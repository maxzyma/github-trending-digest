---
layout: home
title: GitHub Trending Digest
---

# GitHub Trending Digest

每日追踪 GitHub Trending，不只搬运榜单——对每个首次上榜项目做 **社区 Grounding**（GitHub Issues + HN + X/Twitter + Reddit 四源交叉验证），标注风险信号，提取真实使用场景。

## Daily Analysis

| 日期 | 项目数 | 分析 |
|------|--------|------|
{% assign analyses = site.static_files | where_exp: "file", "file.path contains '/daily/' and file.path contains '-analysis.md'" | sort: "path" | reverse %}{% for file in analyses %}{% assign date = file.path | split: "/daily/" | last | replace: "-analysis.md", "" %}| {{ date }} | [榜单]({{ site.baseurl }}/daily/{{ date }}) | [**深度分析**]({{ site.baseurl }}/daily/{{ date }}-analysis) |
{% endfor %}

## Weekly Reports

{% assign weeklies = site.static_files | where_exp: "file", "file.path contains '/weekly/'" | sort: "path" | reverse %}{% for file in weeklies %}{% unless file.path contains ".gitkeep" %}- [{{ file.path | split: "/weekly/" | last | replace: ".md", "" }}]({{ site.baseurl }}/weekly/{{ file.path | split: "/weekly/" | last | replace: ".md", "" }})
{% endunless %}{% endfor %}

## Methodology

每个首次上榜项目必须经过四源验证：

1. **GitHub API** — stars/watchers 比、open issues、贡献者集中度
2. **Hacker News** — 技术社区深度评价
3. **X/Twitter** — 传播路径、KOL 背书、作者推广
4. **Reddit** — 垂直社区真实反馈（r/programming, r/LocalLLaMA 等）

信源强度标注：**强**（2+ 外部信源交叉）/ **中**（单一外部信源）/ **弱**（仅 README）

---

[Analysis Rules & Templates](https://github.com/maxzyma/github-trending-digest/blob/main/README.md) · [GitHub Repo](https://github.com/maxzyma/github-trending-digest)
