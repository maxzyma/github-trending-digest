# GitHub Trending Digest

Daily deep analysis of GitHub Trending: what is trending, why it is spreading, and how reliable the signal is.

Published site: <https://trending.theuntold.ai/>

Sister site: <https://theuntold.ai/> — AI-era critical media analysis, sharing the same visual identity.

## What This Is

GitHub Trending Digest publishes daily, weekly, and monthly analysis of GitHub Trending. It is not only a ranked list. The analysis explains the projects, the surrounding community signal, and the risks behind fast-moving star growth.

The goal is to help readers answer three questions:

- What appeared on GitHub Trending today?
- Which projects or technical themes are worth paying attention to?
- Which popularity signals need cautious interpretation?

## How To Read

- `daily/YYYY-MM-DD.md`: raw daily GitHub Trending list.
- `daily/YYYY-MM-DD-analysis.md`: deep daily analysis with new-project grounding and risk tags.
- `weekly/YYYY-WNN.md`: weekly synthesis across daily reports.
- `monthly/YYYY-MM.md`: monthly synthesis.
- `index.md`: site index used by GitHub Pages.

## Method

For newly tracked projects, the analysis checks more than README claims:

- GitHub stars, subscribers/watchers, issues, pull requests, and contributor concentration.
- Hacker News discussion when available.
- X/Twitter propagation and author or KOL amplification.
- Reddit and vertical community feedback where discoverable.
- Risk tags such as `vanity`, `compliance`, `cost`, `dependency`, `privacy`, `stability`, and `bus_factor`.

Trending is treated as a short-term attention signal, not proof of real adoption. High stars can be meaningful, but the analysis also looks for grounding in usage, issues, external discussion, and maintenance activity.

## Repository Layout

```text
github-trending-digest/
├── README.md          # Human-facing project overview
├── CLAUDE.md          # Claude generation rules and content templates
├── _config.yml        # Jekyll site config
├── _layouts/          # Jekyll layouts
├── assets/            # CSS and brand assets
├── index.md           # Site home page
├── daily/             # Daily raw lists and deep analysis
├── weekly/            # Weekly reports
├── monthly/           # Monthly reports
├── outbox/            # Local DingTalk-derived messages, not public content
└── repos/             # Local submodules for source analysis, excluded from Pages
```

## Maintainers

Content generation rules live in `CLAUDE.md`. DingTalk publishing and webhook workflow rules live in the `github-trends` skill.

Keep this README focused on human readers. Do not add agent runbooks, generation templates, webhook details, or brittle parser constraints here.
