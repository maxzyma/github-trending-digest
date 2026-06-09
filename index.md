---
layout: home
title: GitHub Trending Digest
---

每个首次上榜项目必须经过四源验证：

1. **GitHub API** — stars/watchers 比、open issues、贡献者集中度
2. **Hacker News** — 技术社区深度评价
3. **X/Twitter** — 传播路径、KOL 背书、作者推广
4. **Reddit** — 垂直社区真实反馈（r/programming、r/LocalLLaMA 等）

信源强度：**强**（2+ 外部信源交叉）/ **中**（单一外部信源）/ **弱**（仅 README）

风险标签闭集（7 类）：`vanity` / `compliance` / `cost` / `dependency` / `privacy` / `stability` / `bus_factor`，闭集之外允许自由 tag 归到"其他"。

---

[Analysis Rules](https://github.com/maxzyma/github-trending-digest/blob/main/README.md) · [GitHub Repo](https://github.com/maxzyma/github-trending-digest)

---

## Weekly Reports

- [2026-W23](weekly/2026-W23) — Agent 全栈工具化吃满整张榜（harness/记忆/省 token/UI/数据接入/沙箱六层）；Vanity 密度逐日攀升创纪录（6/06 16/17 = 94%），MemPalace 把名人+加密币+benchmark 造假做成刷星闭环；vanity 判据成熟为组合判据 + 6/07「虚高在前真货在后」两极分化（svelte/nginx/go/whisper/vite 首入却沉腰部）；大厂借 Build 2026 集中投放；Agent 安全议题从 flowsint（critical RCE）与 microsoft/mxc（OS 级隔离）两端浮现

## Daily Analysis

- [2026-06-09](daily/2026-06-09-analysis) — 官方厂商 agent skill 仓成新形态：google/skills（Cloud Next 2026 发布）与 openai/plugins 同框，思路一致——"按需取用知识包"对抗 MCP context bloat；昨日掉榜的 agent/skill 项目（Agent-Reach/PAI/career-ops/mempalace/CopilotKit）集体回流，last30days-skill 单日 +3,558 继续霸榜；skill 生态从"个人刷榜"向"官方+垂类(pm-skills)+工具(whichllm)"分层；解读提醒：高 stars/subs 比值需分两类看——whichllm 251:1 但有真实工程足迹 vs career-ops 244:1 三零有机讨论
- [2026-06-08](daily/2026-06-08-analysis) — AI agent/skill 工具仍占榜单主体但今日以老项目回流为主（last30days 蝉联 + taste-skill/hermes-agent/goose 回榜，新 skill 面孔暂歇）；知识管理（tolaria 16 天破万星/open-notebook）与底层基础设施（opencv/llama.cpp/pg_durable）两簇同步回流；短龄项目 vanity 密度持续（pg_durable 372:1/tolaria 370:1/taste-skill 308:1），turbovec 核心 TurboQuant 算法被 RaBitQ 作者复现质疑、pg_durable 经 HN 467 分但被指无法单测
- [2026-06-07](daily/2026-06-07-analysis) — 榜单结构性两极分化：头部 vanity 膨胀的 agent/skill 仓（superpowers 260:1/219K、Agent-Reach 315:1）vs svelte/nginx/go/whisper/vite 五个真有机老项目首入 tracker 却挤在腰部、日增仅 20–30；career-ops 2 个月 49K stars + HN/Reddit/X 三零 = 继 ECC 后又一教科书级 vanity；microsoft/mxc agent OS 级强制隔离登榜（OpenAI/NVIDIA/Copilot CLI 为启动伙伴）
- [2026-06-06](daily/2026-06-06-analysis) — vanity 密度再创纪录（16/17 > 100:1，94%）；MemPalace 把刷星做成闭环（名人+加密币+benchmark 造假被证伪+pump-and-dump），与 ECC（纯静默刷）、MiroFish（融资故事）三路径同框；star 两极：KOL 挂招牌（flue 349:1）vs 真实企业采纳（CopilotKit AG-UI + $27M）；agent 基础设施近乎霸榜
- [2026-06-05](daily/2026-06-05-analysis) — vanity 密度创纪录（14 选 13 个 >100:1，唯一 organic 是 9 岁的 coding-interview-university 41:1）；agent 基础设施赛道扎堆（6 项）；微软/GitHub 官方借 Build 2026 集中投放（copilot-sdk GA + openclaw-windows-node + spec-kit）
- [2026-06-03](daily/2026-06-03-analysis) — vanity 密度创高（11 选 5）；flowsint critical RCE + license 口径矛盾；headroom 以「Netflix 省 90% token」登顶却社区零讨论，agent harness 省 token 赛道头部化但口碑断层
- [2026-06-02](daily/2026-06-02-analysis) — AI coding agent / harness 生态密集占榜（8/17），5 个实质 NEW 全部「名人 / 媒体 / KOL 投放」驱动——vanity 已从「空壳刷星」演化为「真实产品 + 放大器」
- [2026-05-28](daily/2026-05-28-analysis) — harness 子赛道双极端样本同框（superpowers RE vs claude-code-harness NEW）；heretic 让 LLM 去审查/abliteration 以 HN 745 分登榜；iii=Motia 改名 closed-core 收割
- [2026-05-27](daily/2026-05-27-analysis) — Plex 涨价点燃 jellyfin 迁移 + 5 个免费替代付费服务同框；ppf-contact-solver 真实科研产出登榜成反例标尺；FreeDomain 786:1 vanity 绝对新高
- [2026-05-26](daily/2026-05-26-analysis) — 「反 AI slop」双胞胎同框；Anthropic 官方两连；ECC 4 个月 19 万 stars + HN/Reddit 双零；gstack 100K 里程碑兑现
- [2026-05-22](daily/2026-05-22-analysis) — 榜单罕见零 NEW 项目全延续；codegraph 单日 +4,294⭐ 引爆代码知识图谱赛道
- [2026-05-21](daily/2026-05-21-analysis) — 官方技能包矩阵再扩张；WhatsApp 自托管 API 回潮；12 NEW 占 63%
- [2026-05-20](daily/2026-05-20-analysis) — 反 Adobe + 反 SaaS + 反订阅三浪同框；phantomstars 议题首次浮现
- [2026-05-19](daily/2026-05-19-analysis) — agent-skills 漏斗矩阵扩展
- [2026-05-18](daily/2026-05-18-analysis) — 老牌自托管 OSS 集体回潮
