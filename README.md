# GitHub Trends 跟踪规则

_最后更新: 2026-03-31_

## 目录结构

```
github-trends/
├── README.md          # 本文件（规则定义）
├── repos/             # 子模块（trending 项目源码）
├── daily/             # 每日文件
│   ├── YYYY-MM-DD.md          # 原始榜单（项目名 + Stars + 排名变化）
│   └── YYYY-MM-DD-analysis.md # 逐项分析（去重，已上榜项目只做增量更新）
├── weekly/            # 每周文件（周一生成，覆盖上一周 Mon~Sun）
│   └── YYYY-WNN.md            # 周趋势总结
└── monthly/           # 每月文件（月初生成，覆盖上一月）
    └── YYYY-MM.md             # 月趋势总结
```

## 每日原始榜单 — `daily/YYYY-MM-DD.md`

记录当天 GitHub Trending 的原始数据，不做分析。

```markdown
# GitHub Trending 每日榜单 — YYYY 年 M 月 D 日（周X）

| # | 项目 | Stars | 今日 | 排名变化 |
|---|------|-------|------|---------|
| 1 | owner/repo | 5,900 | +120 | NEW |
| 2 | owner/repo | 12,300 | +85 | =  |
| 3 | owner/repo | 800 | +200 | ↑3 |
```

排名变化标记：
- `NEW` — 首次上榜
- `RE` — 重新上榜（此前上过榜又掉出，今天回来）
- `=` — 排名不变
- `↑N` / `↓N` — 排名上升/下降 N 位

## 每日分析 — `daily/YYYY-MM-DD-analysis.md`

对当日榜单中的项目做逐项分析，**去重**处理。

### 去重规则

- **首次上榜**（NEW）：完整分析（技术栈、核心价值、亮点、局限、目标用户）
- **已上过榜**（=、↑、↓、RE）：仅写增量更新（Stars 变化、新版本、新功能、社区动态等）
- 判断依据：检索 `daily/` 下历史分析文件，项目名（owner/repo）匹配即视为"已上榜"

### 分析文档标题格式

```markdown
# GitHub Trending 深度分析 — YYYY 年 M 月 D 日（周X）

_一句话概括今日最值得关注的趋势或事件_

_项目总数: N | 首次上榜: N | 已上榜更新: N | 数据源: https://github.com/trending_
```

标题要求：**可独立发布**——脱离目录结构也能看懂是什么、什么时间、什么来源。副标题用一句话抓住读者。

### 首次上榜模板

**写作原则**：读者可能完全不知道这个项目。每条分析必须让零背景的人在 30 秒内理解：这东西是什么、解决什么问题、谁在用、值不值得关注。

```markdown
### [owner/repo](https://github.com/owner/repo) — NEW ⭐ N（+M）| 语言 | 信源：强/中/弱

**它是什么**: 用一段非技术语言解释这个项目做什么。想象你在向一个非程序员的同事解释。
避免："基于 X 框架的 Y 平台"。改用："帮你做 Z 这件事的工具"。

**解决什么问题**: 没有这个项目之前，用户怎么解决这个问题？用了之后有什么不同？

**谁在用、怎么用**（从 Issues/HN/Reddit 提取真实场景）:
- 场景 1: 具体描述（引用 Issue 编号或 HN 用户名）
- 场景 2: ...

**社区怎么评价**:
- 👍 正面: ...（引用信源）
- 👎 负面: ...（引用信源）
- 📊 健康度: stars/watchers 比、open issues、维护状态等关键指标

**风险与争议**: 只写重要的，不堆砌

**技术备注**: 语言/框架/协议等，放最后，给需要的人看
```

### 社区 Grounding 方法

对每个首次上榜项目，**必须**执行以下信源检查（不能仅靠 README）：

1. **GitHub API**（必选）:
   - `gh api repos/{owner}/{repo}` → stars/forks/watchers/open_issues
   - `gh api repos/{owner}/{repo}/issues?state=open&sort=comments&per_page=5` → 最热 issues
   - 关注异常信号：Stars/Watchers 比 >100:1、PR 零合并、Open Issues 积压
2. **Hacker News**（必选）:
   - `https://hn.algolia.com/api/v1/search?query={repo_name}&tags=story`
   - 有讨论 → 提取核心观点；无讨论 → 记录"HN 无讨论"（本身是信号）
3. **X/Twitter**（必选）:
   - WebSearch `{repo_name} site:x.com` 或 `{repo_name} twitter`
   - 关注：作者/官方推广帖的互动量、开发者真实使用反馈、批评声音
   - 许多项目的传播主要在 X 而非 HN——不查 X 就无法解释 star 来源
4. **Reddit**（必选）:
   - WebSearch `{repo_name} site:reddit.com`（不用直接 API，会被拦截）
   - 关注 r/programming、r/LocalLLaMA、r/selfhosted、r/netsec 等垂直社区的真实讨论
   - 这些垂直社区的深度反馈是 HN 和 X 覆盖不到的

信源可信度标注：
- **强**：GitHub Issues + HN/X 至少两个外部信源交叉验证
- **中**：仅 GitHub Issues 或仅单一外部信源（HN 或 X）
- **弱**：仅 README 分析，无社区验证（必须标注"无信源，基于推断"）

### 已上榜更新模板

```markdown
### owner/repo — ↑3（连续上榜 N 天）

- **Stars**: N（今日 +M，累计 +K since 首次上榜日）
- **更新**: 新版本 / 新功能 / 社区事件等（无变化则写"无显著更新"）
```

## 每周总结 — `weekly/YYYY-WNN.md`

**生成时机**: 每周一，覆盖上一周（Mon~Sun）

### 内容结构

```markdown
# GitHub Trending 周报 — YYYY 第 NN 周（M月D日 ~ M月D日）

_一句话概括本周最核心的趋势变化_

## 本周趋势纵览
（2-3 段总结本周整体趋势，与上周对比变化）

## 分类分析
| 分类 | 项目 | 趋势判断 |
|------|------|---------|
（按技术领域分类，标注上升/稳定/下降）

## 本周新面孔
（首次上榜的项目列表及简要点评）

## 持续热门
（连续多天上榜的项目，分析为什么持续热门）

## 值得关注的信号
（3-5 条趋势洞察，结合分类数据和排名变化推断）
```

## 每月总结 — `monthly/YYYY-MM.md`

**生成时机**: 每月 1 日，覆盖上一个自然月

### 内容结构

与周总结维度一致，可额外增加：

```markdown
# GitHub Trending 月报 — YYYY 年 M 月

_一句话概括本月最核心的趋势变化_

## 月度趋势纵览

## 分类分析

## 月度新面孔 Top 10

## 持续热门 Top 10

## 值得关注的信号

## 月度额外维度（可选）
- **技术栈分布**: 语言/框架占比变化
- **组织类型分布**: 个人 vs 公司 vs 基金会
- **Star 增长排行**: 本月绝对增长 Top 10
- **地域信号**: 中国/美国/欧洲项目占比
- **生态关联**: 哪些平台/框架的生态项目最多
```

## 数据源说明

- 数据来源：https://github.com/trending（daily 维度）
- GitHub Trending 每日展示的项目数量不固定（观测范围 4~14 个），按实际展示数量分析

## 子模块管理

- 新上榜项目**按需** clone 为子模块到 `repos/`（用于源码分析）
- **知名老项目**（freeCodeCamp、sherlock 等）无需 clone，基于已知信息分析即可
- 已有子模块不重复添加
- 使用 `--depth 1` 浅克隆节省空间
- 长期不上榜的子模块可定期清理（月度总结时评估）

## 操作流程

```
每日（数据采集后）:
  1. 写 daily/YYYY-MM-DD.md（原始榜单）
  2. 新项目 → git submodule add --depth 1 到 repos/
  3. 分析 → 写 daily/YYYY-MM-DD-analysis.md（去重）

每周一:
  4. 汇总上周 daily/ → 写 weekly/YYYY-WNN.md

每月 1 日:
  5. 汇总上月 weekly/ → 写 monthly/YYYY-MM.md
```

## 收尾流程（所有模式通用）

文档写完、钉钉发送后，按顺序执行以下步骤。

### 更新 index.md

在本目录 `index.md` 对应章节**下方第一行**插入新链接：

| 模式 | 章节 | 格式 |
|------|------|------|
| Daily | `## Daily Analysis` | `- [YYYY-MM-DD](daily/YYYY-MM-DD-analysis) — 副标题` |
| Weekly | `## Weekly Reports` | `- [YYYY-WNN](weekly/YYYY-WNN) — 副标题`（参照已有条目） |
| Monthly | `## Monthly Reports` | `- [YYYY-MM](monthly/YYYY-MM) — 副标题`（如无该章节，在 Weekly Reports 之后新建） |

### 两层提交推送

本目录是 coworkspace 的子模块，push 需要两层：

```bash
# 1) 子模块内提交推送
git add .
git commit -m "feat: add {mode} analysis YYYY-MM-DD"
git push  # dangerouslyDisableSandbox: true

# 2) 回到父仓库更新引用
cd $(git rev-parse --show-superproject-working-tree)
git add notes/02-调研/github-trends
git commit -m "chore: update github-trending-digest ref"
git push  # dangerouslyDisableSandbox: true
```
