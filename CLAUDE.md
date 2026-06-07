# Claude Instructions

This file is the source of truth for generating and editing GitHub Trending Digest content. `README.md` is human-facing and must not be used as the generation rulebook.

## Project Purpose

Turn GitHub Trending into publishable analysis that explains:

- What projects and themes are trending.
- Why the attention is happening.
- How grounded the signal is in real community activity.
- Which projects need cautious interpretation.

Preserve the core value of the project: community grounding, risk labeling, and clear separation between popularity and adoption.

## Narrative Order

Daily analysis should first help readers understand "what is on the list today" and then help them interpret signal quality.

Critical analysis must stay, but it should not be the only opening frame.

Use this order by default:

1. State the day's visible structure in neutral language: major categories, NEW/RE counts, notable projects, and obvious theme clusters.
2. Explain the most important trend lines.
3. Then introduce reliability concerns: high stars/subscribers ratios, thin issues, weak HN/X/Reddit grounding, young repo age, marketing-heavy propagation.
4. Keep strong negative judgments inside project analysis or a dedicated signal-quality section, not as the only entry point.

For example, prefer:

> Today combines high-spread AI agent projects with a return of mature infrastructure projects. Several short-lived AI repos also require cautious interpretation because stars, subscribers, issues, and public community discussion do not line up.

Avoid opening only with:

> The list is dominated by vanity-inflated projects.

## Daily Raw List: `daily/YYYY-MM-DD.md`

Record the raw GitHub Trending data without analysis.

```markdown
# GitHub Trending 每日榜单 — YYYY 年 M 月 D 日（周X）

| # | 项目 | Stars | 今日 | 排名变化 |
|---|------|-------|------|---------|
| 1 | [owner/repo](https://github.com/owner/repo) | 5,900 | +120 | NEW |
| 2 | [owner/repo](https://github.com/owner/repo) | 12,300 | +85 | = |
| 3 | [owner/repo](https://github.com/owner/repo) | 800 | +200 | ↑3 |

> 数据源：<https://github.com/trending> · 抓取于 YYYY-MM-DD
```

Ranking markers:

- `NEW`: first time in this tracker.
- `RE`: previously tracked, dropped out, and returned.
- `=`: unchanged rank.
- `↑N` / `↓N`: rank moved up/down by N.

## Daily Analysis: `daily/YYYY-MM-DD-analysis.md`

Analyze each project with de-duplication.

### De-Duplication

- `NEW`: full analysis.
- `RE`, `=`, `↑`, `↓`: incremental update only.
- Determine prior appearance by exact `owner/repo` match in historical `daily/*-analysis.md` files.
- Mature well-known projects that first enter this tracker can be recorded as "知名老项目首入 tracker" without full community grounding.

### Title Format

```markdown
# GitHub Trending 深度分析 — YYYY 年 M 月 D 日（周X）

_一句话概括今日最值得关注的趋势或事件_

_项目总数: N | 首次上榜: N | 重新上榜: N | 已上榜更新: N | 数据源: https://github.com/trending_
```

The subtitle should attract readers by explaining the day, not by starting only from a critique. It can mention reliability concerns, but should also name the concrete trends or projects.

### Required Top Section: `## 本日主线`

After the title and metadata, include `## 本日主线`. The heading name is fixed because downstream parsing depends on it. Do not rename it to similar headings such as `## 今日主线`, `## 今日趋势观察`, or `## 今日核心信号`.

Rules:

- Use 1-N main lines based on the day. Do not force three lines.
- The first main line should usually be a neutral map of the day's list.
- Later lines can cover signal quality, vanity, marketing amplification, security risks, or other caveats.
- Each main line should include concrete data and one clear judgment.

Template:

```markdown
## 本日主线

**主线一：<主题名> — <一句结论>**。<事实、数据、项目对照、读者视角判断>。

**主线二：<主题名> — <一句结论>**。<事实、数据、项目对照、读者视角判断>。
```

If signal quality is a major issue, use a distinct main line such as:

```markdown
**主线三：榜单解读提醒 — Trending 热度不等于真实采用。** ...
```

## New Project Template

Readers may know nothing about the project. Each NEW item must let a zero-background reader understand what it is, what problem it solves, who appears to be using it, and whether it deserves attention.

```markdown
### [owner/repo](https://github.com/owner/repo) — NEW ⭐ N（+M）| Language | 信源：强/中/弱

**它是什么**: 用非技术语言解释这个项目做什么。避免只写"基于 X 的 Y 平台"。

**解决什么问题**: 没有这个项目之前，用户如何解决问题？用了之后有什么不同？

**谁在用、怎么用**（来自 Issues/HN/Reddit/X/评测）:
- 场景 1: 具体使用场景，引用 issue 编号或外部讨论。
- 场景 2: 具体使用场景，引用 issue 编号或外部讨论。

**社区怎么评价**:
- 正面: ...
- 负面: ...
- 健康度: stars/subscribers 比、open issues、PR、维护状态、贡献者集中度。

**风险与争议**:
- **<tag>**: <一句话说明>
- **<tag>**: <一句话说明>

**技术备注**: 语言、框架、协议、部署方式等，放最后。
```

## Community Grounding

For every NEW project, check these sources unless it is a mature well-known project recorded only as a lightweight tracker entry:

1. GitHub API:
   - `gh api repos/{owner}/{repo}` for stars, forks, subscribers/watchers, open issues, creation date, pushed date.
   - `gh api 'repos/{owner}/{repo}/issues?state=open&sort=comments&per_page=5'` for hot issues.
   - Watch for stars/subscribers > 100:1, stale PRs, concentrated contributors, issue accumulation.
2. Hacker News:
   - `https://hn.algolia.com/api/v1/search?query={repo_name}&tags=story`
   - If no discussion exists, say so. Lack of discussion can be a signal.
3. X/Twitter:
   - Search for `{repo_name} site:x.com` or `{repo_name} twitter`.
   - Distinguish author/KOL promotion from independent developer feedback.
4. Reddit:
   - Search for `{repo_name} site:reddit.com`.
   - Check relevant communities such as r/programming, r/LocalLLaMA, r/selfhosted, r/netsec.

Source strength:

- `强`: GitHub Issues plus at least two external sources.
- `中`: GitHub Issues plus one external source, or one strong external source.
- `弱`: README/code-only inference. Mark clearly as inference.

## Risk Tags

Use markdown bullets with bold tags so dashboard extraction remains reliable:

```markdown
**风险与争议**:
- **vanity**: ...
- **stability**: ...
```

Preferred closed set:

| Tag | Meaning | Typical signal |
|---|---|---|
| `vanity` | 空心化/虚高 | stars rise faster than subscribers, issues, HN/X/Reddit, or usage evidence |
| `compliance` | 合规风险 | license, ToS, regulatory, copyright, data-use risk |
| `cost` | 成本失控 | token/API/commercial pricing risk |
| `dependency` | 依赖风险 | relies on fragile third-party APIs, services, or vendors |
| `privacy` | 隐私 | user data upload, unclear retention, cross-border data flow |
| `stability` | 稳定性 | early alpha, broken installs, regressions, not production-grade |
| `bus_factor` | 维护风险 | single maintainer, stale PRs, contributor concentration |

Free-form tags are allowed when necessary, but prefer the closed set.

Avoid:

- Inline numbered risk paragraphs.
- Long untagged prose under `风险与争议`.
- Treating a high stars/subscribers ratio alone as proof of vanity for very large, mature repos.

## Incremental Update Template

```markdown
### owner/repo — ↑3（连续上榜 N 天）

- **Stars**: N（今日 +M，累计 +K since 首次上榜日）
- **更新**: 新版本 / 新功能 / 社区事件等。无变化则写"无显著更新"。
```

## Weekly Report: `weekly/YYYY-WNN.md`

Generate on Monday for the previous Monday-Sunday range.

```markdown
# GitHub Trending 周报 — YYYY 第 NN 周（M月D日 ~ M月D日）

_一句话概括本周最核心的趋势变化_

## 本周趋势纵览

## 分类分析

## 本周新面孔

## 持续热门

## 值得关注的信号
```

Keep `## 本周趋势纵览` as the top synthesis heading.

## Monthly Report: `monthly/YYYY-MM.md`

Generate at the start of a month for the previous natural month.

```markdown
# GitHub Trending 月报 — YYYY 年 M 月

_一句话概括本月最核心的趋势变化_

## 月度趋势纵览

## 分类分析

## 月度新面孔 Top 10

## 持续热门 Top 10

## 值得关注的信号
```

Optional monthly dimensions:

- 技术栈分布
- 组织类型分布
- Star 增长排行
- 地域信号
- 生态关联

## Frontmatter

After writing an analysis file, run:

```bash
python3 previews/gen-frontmatter.py --apply daily/YYYY-MM-DD-analysis.md
```

If running from the workspace root instead of this repository root, use:

```bash
python3 publications/github-trending-digest/previews/gen-frontmatter.py --apply publications/github-trending-digest/daily/YYYY-MM-DD-analysis.md
```

The script extracts title, subtitle, counts, new repos, updated repos, and risk tags. Do not hand-maintain YAML unless the script cannot run.

## Index Maintenance

After publishing a document, insert the newest link as the first item under the corresponding section in `index.md`.

| Mode | Section | Link format |
|---|---|---|
| Daily | `## Daily Analysis` | `- [YYYY-MM-DD](daily/YYYY-MM-DD-analysis) — subtitle` |
| Weekly | `## Weekly Reports` | `- [YYYY-WNN](weekly/YYYY-WNN) — subtitle` |
| Monthly | `## Monthly Reports` | `- [YYYY-MM](monthly/YYYY-MM) — subtitle` |

## Submodules

- Clone NEW non-famous projects into `repos/` only when source analysis is useful.
- Use shallow clones when possible.
- Do not clone mature, well-known projects solely for lightweight tracker entries.
- Existing submodules should not be duplicated.
- `repos/` is excluded from GitHub Pages builds.

## Tone

Be direct, evidence-based, and readable. Strong claims are allowed when the evidence supports them, but keep the reader's first need in mind: understanding the current GitHub Trending landscape.

Prefer:

- "需要谨慎解读"
- "传播热度强，但社区 grounding 弱"
- "Trending 热度不等于真实采用"

Use sharper labels such as `vanity` when the combination of signals supports it: high ratio, weak community footprint, short repo age, thin issues, and marketing-heavy propagation.
