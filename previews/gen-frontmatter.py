#!/usr/bin/env python3
"""Generate Jekyll frontmatter for github-trending-digest daily analysis files.

Reads `daily/YYYY-MM-DD-analysis.md` (no frontmatter assumed) and emits the
content with a YAML frontmatter block prepended, extracted from the markdown
structure. Body is left byte-for-byte unchanged.

Default: dry-run, write a side-by-side preview to stdout.
With --apply: overwrite the input file in place.
With --frontmatter-only: print only the YAML frontmatter (for inspection).

Extracts:
- date          (from filename)
- title         (H1)
- subtitle      (first italic paragraph after H1)
- total / new_count / updated_count   (italic metadata line)
- new_repos[]:    repo, stars, star_delta, lang, source_strength, risk_tags
- updated_repos[]: repo, change, days_listed

No external dependencies. Stdlib only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Optional


# ─── Regex patterns ─────────────────────────────────────────────────────────

RE_DATE = re.compile(r'(\d{4}-\d{2}-\d{2})')

# Italic metadata line variants:
#   _项目总数：13 | 首次上榜：4 | 已上榜更新：9 | 数据源：…_
#   _项目总数: 14（去重后） | 首次上榜: 14 | 数据源: …_     (early format, no 已上榜更新)
RE_META = re.compile(
    r'项目总数[:：]\s*(?P<total>\d+)[^|]*\|\s*'
    r'首次上榜[:：]\s*(?P<new>\d+)'
    r'(?:[^|]*\|\s*已上榜更新[:：]\s*(?P<updated>\d+))?'
)

# ### [owner/repo](url) — NEW ⭐ X,XXX (+XXX) | Lang | 信源：强/中/弱
# Also matches:
#   - bare form (no markdown link)
#   - early formats: "⭐ 5,900+", "⭐ 31K", "⭐ 18.9K", "⭐ 126K"
RE_NEW_HEADER = re.compile(
    r'^###\s*(?:\[(?P<repo_l>[^\]]+)\]\([^)]+\)|(?P<repo_p>[A-Za-z0-9][\w.-]*/[\w.-]+))\s*[—\-]\s*'
    r'NEW\s*⭐\s*(?P<stars>[\d,]+(?:\.\d+)?[Kk]?)\+?\s*'
    r'(?:[（(]\+(?P<delta>[\d,]+)[）)]\s*)?'
    r'\|\s*'
    r'(?P<lang>[^|]+?)\s*\|\s*信源[:：]\s*(?P<src>强|中|弱)',
    re.MULTILINE,
)


def _parse_stars(s: str) -> int:
    """Parse "12,345" / "31K" / "18.9K" / "5,900" into int."""
    s = s.replace(',', '').strip()
    if s and s[-1] in 'Kk':
        return int(float(s[:-1]) * 1000)
    return int(s)

# ### [owner/repo](url) — ↑N / ↓N / = / RE …
# Also matches the bare form (no markdown link).
RE_UPD_HEADER = re.compile(
    r'^###\s*(?:\[(?P<repo_l>[^\]]+)\]\([^)]+\)|(?P<repo_p>[A-Za-z0-9][\w.-]*/[\w.-]+))\s*[—\-]\s*(?P<rest>.+?)\s*$',
    re.MULTILINE,
)
RE_CHANGE = re.compile(r'(↑\d+|↓\d+|=|RE)')
RE_DAYS = re.compile(r'连续上榜\s*(\d+)\s*天')

# - **xxx**: ...   inside a 风险与争议 block
RE_RISK_TAG = re.compile(r'^-\s*\*\*([^*\n]+?)\*\*\s*[:：]', re.MULTILINE)

# Body of "**风险与争议**:" section — bullets + maybe nested bullets, until next bold heading or section
RE_RISK_BLOCK = re.compile(
    r'\*\*风险与争议\*\*\s*[:：](.+?)(?=\n\*\*[^*]+?\*\*\s*[:：]|\n##|\n---|\Z)',
    re.DOTALL,
)

RE_H1 = re.compile(r'^#\s+(.+?)\s*$', re.MULTILINE)


# ─── Parsers ────────────────────────────────────────────────────────────────

def parse_section(text: str, *prefixes: str) -> str:
    """Return body under any `## <prefix>...` heading until the next `##`.

    Tries prefixes in order; first match wins. Uses prefix matching to
    handle historical variants like:
        ## 首次上榜项目
        ## 首次上榜（NEW，6 个）
        ## NEW 项目逐项分析
    """
    for prefix in prefixes:
        pat = re.compile(
            rf'^##\s+{re.escape(prefix)}.*?$\n(.*?)(?=^##\s|\Z)',
            re.MULTILINE | re.DOTALL,
        )
        m = pat.search(text)
        if m:
            return m.group(1)
    return ''


def parse_subtitle(text: str) -> str:
    """First _italic_ paragraph after the H1 that isn't the metadata line."""
    seen_h1 = False
    for raw in text.splitlines():
        line = raw.strip()
        if not seen_h1:
            if line.startswith('# '):
                seen_h1 = True
            continue
        if not line:
            continue
        if line.startswith('_') and line.endswith('_') and len(line) > 2:
            inner = line[1:-1]
            if '项目总数' in inner or '数据源' in inner:
                continue
            return inner.strip()
        # Stop after first non-italic content paragraph
        if not line.startswith('_'):
            return ''
    return ''


def parse_new_projects(section: str) -> list[dict]:
    """Each ### NEW header → dict. Risk tags from the project's 风险与争议 block."""
    headers = list(RE_NEW_HEADER.finditer(section))
    out = []
    for i, m in enumerate(headers):
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(section)
        block = section[start:end]
        risk_tags: list[str] = []
        rb = RE_RISK_BLOCK.search(block)
        if rb:
            risk_tags = [t.strip() for t in RE_RISK_TAG.findall(rb.group(1))]
        delta = m.group('delta')
        out.append({
            'repo': (m.group('repo_l') or m.group('repo_p')).strip(),
            'stars': _parse_stars(m.group('stars')),
            'star_delta': int(delta.replace(',', '')) if delta else 0,
            'lang': m.group('lang').strip(),
            'source_strength': m.group('src'),
            'risk_tags': risk_tags,
        })
    return out


def parse_updated_projects(section: str) -> list[dict]:
    out = []
    seen = set()
    for m in RE_UPD_HEADER.finditer(section):
        repo = (m.group('repo_l') or m.group('repo_p')).strip()
        if repo in seen:
            continue
        rest = m.group('rest')
        cm = RE_CHANGE.search(rest)
        if not cm:
            # e.g. "见上方 NEW 项目分析" cross-references — skip
            continue
        dm = RE_DAYS.search(rest)
        out.append({
            'repo': repo,
            'change': cm.group(1),
            'days_listed': int(dm.group(1)) if dm else None,
        })
        seen.add(repo)
    return out


def parse_metadata(text: str) -> dict:
    m = RE_META.search(text)
    if not m:
        return {}
    out = {
        'total': int(m.group('total')),
        'new_count': int(m.group('new')),
    }
    upd = m.group('updated')
    if upd is not None:
        out['updated_count'] = int(upd)
    return out


def parse_title(text: str) -> str:
    m = RE_H1.search(text)
    return m.group(1).strip() if m else ''


def date_from_filename(path: Path) -> Optional[str]:
    m = RE_DATE.search(path.name)
    return m.group(1) if m else None


# ─── YAML emitter (no PyYAML dependency) ────────────────────────────────────

def _quote(s: str) -> str:
    s = str(s)
    needs_quote = (
        s == ''
        or s.strip() != s
        or s in ('null', 'true', 'false', '~', 'yes', 'no', 'on', 'off')
        # YAML reserved single-char tags / indicators that confuse parsers
        or s in ('=', '?', '*', '&', '|', '>', '!', '%', '@', '`')
        or s[0] in '!&*[]{}|>%@`#,?='
        or ': ' in s
        or s.endswith(':')
    )
    if needs_quote:
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def _scalar(v) -> str:
    if v is None:
        return 'null'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return str(v)
    return _quote(str(v))


def _list_inline(v: list) -> str:
    """Inline flow list. String items are always single-quoted to avoid
    YAML mis-parsing on '#' (comment), ',' (separator), '"', etc."""
    if not v:
        return '[]'
    parts = []
    for x in v:
        if x is None:
            parts.append('null')
        elif isinstance(x, bool):
            parts.append('true' if x else 'false')
        elif isinstance(x, (int, float)):
            parts.append(str(x))
        else:
            s = str(x)
            parts.append("'" + s.replace("'", "''") + "'")
    return '[' + ', '.join(parts) + ']'


def emit_yaml(data: dict, indent: int = 0) -> str:
    pad = '  ' * indent
    lines = []
    for k, v in data.items():
        if isinstance(v, dict):
            lines.append(f'{pad}{k}:')
            if v:
                lines.append(emit_yaml(v, indent + 1))
            else:
                lines[-1] += ' {}'
        elif isinstance(v, list) and v and isinstance(v[0], dict):
            lines.append(f'{pad}{k}:')
            for item in v:
                first = True
                for ik, iv in item.items():
                    if first:
                        prefix = f'{pad}  - '
                        first = False
                    else:
                        prefix = f'{pad}    '
                    if isinstance(iv, list):
                        lines.append(f'{prefix}{ik}: {_list_inline(iv)}')
                    else:
                        lines.append(f'{prefix}{ik}: {_scalar(iv)}')
        elif isinstance(v, list):
            lines.append(f'{pad}{k}: {_list_inline(v)}')
        else:
            lines.append(f'{pad}{k}: {_scalar(v)}')
    return '\n'.join(lines)


# ─── Main ───────────────────────────────────────────────────────────────────

def build_frontmatter(text: str, path: Path) -> dict:
    fm: dict = {'layout': 'daily'}
    date = date_from_filename(path)
    if date:
        fm['date'] = date
    fm['title'] = parse_title(text)
    subtitle = parse_subtitle(text)
    if subtitle:
        fm['subtitle'] = subtitle
    fm.update(parse_metadata(text))
    # prefix-match: "首次上榜" matches both "首次上榜项目" and "首次上榜（NEW，6 个）"
    new_section = parse_section(text, '首次上榜', 'NEW 项目', '新项目')
    upd_section = parse_section(text, '已上榜更新', '已上榜项目', '更新项目')
    # Early format (e.g. 2026-03-30) has no H2 grouping — every ### is a NEW project.
    # Fallback: if no NEW section found, scan whole document for NEW project headers.
    if not new_section:
        new_section = text
    fm['new_repos'] = parse_new_projects(new_section)
    fm['updated_repos'] = parse_updated_projects(upd_section)
    return fm


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument('files', nargs='+', help='daily/YYYY-MM-DD-analysis.md')
    ap.add_argument('--apply', action='store_true', help='Overwrite files in place')
    ap.add_argument('--force', action='store_true',
                    help='Force re-apply even if frontmatter already exists (strips old, generates new)')
    ap.add_argument('--frontmatter-only', action='store_true',
                    help='Print only the YAML frontmatter')
    args = ap.parse_args(argv)

    rc = 0
    for f in args.files:
        path = Path(f)
        if not path.exists():
            print(f'! not found: {path}', file=sys.stderr)
            rc = 1
            continue
        text = path.read_text(encoding='utf-8')
        if text.startswith('---\n'):
            if not args.force:
                print(f'! already has frontmatter, skipped: {path}', file=sys.stderr)
                continue
            # strip existing frontmatter
            end = text.find('\n---\n', 4)
            if end > 0:
                text = text[end + 5:]
                if text.startswith('\n'):
                    text = text[1:]

        fm = build_frontmatter(text, path)
        yaml_block = emit_yaml(fm)
        new_content = f'---\n{yaml_block}\n---\n\n{text}'

        if args.frontmatter_only:
            sep = '═' * 50
            print(f'{sep}\n{path.name}\n{sep}')
            print(f'---\n{yaml_block}\n---')
            print()
        elif args.apply:
            path.write_text(new_content, encoding='utf-8')
            print(f'✓ updated in place: {path}', file=sys.stderr)
        else:
            sep = '═' * 50
            print(f'{sep}\n{path.name}\n{sep}')
            print(new_content[:3500])
            if len(new_content) > 3500:
                print(f'\n... [truncated, full size {len(new_content)} chars]')
            print()
    return rc


if __name__ == '__main__':
    sys.exit(main())
