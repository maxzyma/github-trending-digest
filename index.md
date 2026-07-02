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

## Monthly Reports

- [2026-06](monthly/2026-06) — agent/skills 生态大厂化（OpenAI/Google/Anthropic/AWS/阿里官方项目同月在榜，月末落地 design.md/claude-plugins-official/page-agent 权威锚点）+ vanity 方法论完成收口（高 ratio 单指标 → 组合判据 → 比值是入口信号结论靠足迹 → 模板复制/厂商主导/真营销驱动三成因）；最扎实真信号是成熟基础设施集中回流（apple/container/firecrawl/MinerU/MediaCrawler/Stirling-PDF）+ 事件驱动双强发版（GLM-5 HN 883 分/iroh HN 1,351 分/LMCache 生产集成）；最需谨慎是短龄高失衡投资·交易·视频仓（ECC 198:1/MemPalace 造假闭环/OpenMontage 五天涨 13K/TREK 481:1/ai-berkshire 397:1）；数据侧持续恶化（全月缺 6 天 + 周末 cron 空档连续三周 + 脚本连续三日误标全 NEW）

## Weekly Reports

- [2026-W26](weekly/2026-W26) — 头部格局较 W25 更稳：AI 创作/视频守榜首（OpenMontage 连续五天领跑单日增量 +987→+3,434，五天涨 13K stars）；本周最扎实真信号是成熟开源工具几乎天天回流/首入 tracker（spiderfoot/firecrawl/Stirling-PDF/apple-container/MinerU/CasaOS/MediaCrawler），回流主体从 W25 的 SaaS 替代品转向数据/文档/抓取基础设施；agent/skills 稳定占约半数且大厂化（Anthropic 官方 plugins 目录/Google design.md ↑9 至 #1/AWS agent-toolkit/阿里 page-agent HN 147 分）；短龄高比值仓集中涌现（hyperframes 366:1/ai-website-cloner 198:1/TREK 481:1/ai-berkshire 397:1），方法论细化为模板复制/厂商主导/真营销驱动三成因；数据双重恶化：周六+周日双缺漏、脚本连续三日误标全部 NEW（已人工校正）
- [2026-W25](weekly/2026-W25) — W24 末悬念「去 agent 化是拐点还是波动」收口为「波动」：6/17 agent 本体彻底挂零，6/18 agent/skills 框架（superpowers 231K/mattpocock 133K/codebase-memory-mcp）一天强势反转打回三天趋势；新增主线开源模型真发版集体回归（GLM-5/GLM-5.2 登 Artificial Analysis 开源权重榜首 + SWE-bench 超 GPT-5.5 + MIT、LTX-2 音视频联合生成单卡可跑）；iroh 1.0（HN 1,351 分 + Holochain/Fedimint 真采用）跨三天领跑事件驱动；成熟开源 SaaS 替代品两轮整齐回潮（penpot/insomnia/twenty/RocketChat/plane）；6/20 给出可信度三档分层模板（真信号/需结合足迹/收藏型）；6/21 周日再缺漏（与 6/14 连续两周）
- [2026-W24](weekly/2026-W24) — 榜单明显「去 agent 化」：新弹药连续转出 agent/skill 赛道（CV/医疗 AI/边缘感知/系统容器/自托管/LLM 推理缓存），6/10·6/13 两天真 NEW 全在 agent 之外；apple/container 借 WWDC26 + 1.0 + HN 1,197 分三连击 ↑16 登顶；agent 安全对偶落地（NVIDIA/SkillSpector skill 安全扫描进 ClawHub 流水线）；vanity 判据收口为「比值是入口信号、结论靠足迹」（LMCache/openmed/espectre 高比值真采用对照 career-ops/zhangxuefeng-skill 传播型热度）；成熟基础设施借发版集体回流（restic/mattermost/chatwoot/fanqiang/PowerToys）
- [2026-W23](weekly/2026-W23) — Agent 全栈工具化吃满整张榜（harness/记忆/省 token/UI/数据接入/沙箱六层）；Vanity 密度逐日攀升创纪录（6/06 16/17 = 94%），MemPalace 把名人+加密币+benchmark 造假做成刷星闭环；vanity 判据成熟为组合判据 + 6/07「虚高在前真货在后」两极分化（svelte/nginx/go/whisper/vite 首入却沉腰部）；大厂借 Build 2026 集中投放；Agent 安全议题从 flowsint（critical RCE）与 microsoft/mxc（OS 级隔离）两端浮现

## Daily Analysis

- [2026-07-02](daily/2026-07-02-analysis) — AI2 官方 OCR 工具 olmocr 首入是今日 grounding 最扎实的真信号（HN 313 分，PDF→LLM 语料，Reducto 二次开发采用）；腾讯 CubeSandbox（AI agent microVM 沙箱/E2B 替代）与之同日首入，标志「AI agent 基础设施」大厂化延续（接续昨日 Meta astryx ↑11 / Google agents-cli）；安全·渗透工具持续同框（strix 守 rank 2 / VulnClaw 回归双仓 / cupp）；短龄高失衡 AI 交易·视频·语音·议事 agent 延续（herdr 419:1 / FluidVoice 345:1 / exercises-dataset 302:1 / OmniRoute 299:1 / council 190:1）需谨慎；脚本继续全 20 项误标 NEW 已人工校正（真 NEW 3：olmocr/CubeSandbox/karukan，RE 5：logto/VulnClaw/tolaria/council/AiToEarn）
- [2026-07-01](daily/2026-07-01-analysis) — 终端多 agent 编排 herdr 为今日 grounding 最扎实真信号（Rust，Show HN 161 分/101 评，取代十几个终端窗口/比 tmux 好用）；Meta astryx 与 Google agents-cli 同日推出「agent-ready」基础件（设计系统 manifest / Google Cloud ADK agent 脚手架，官方主导传播）；安全·隐私工具持续同框（strix AI 渗透回归 / cupp 经典密码字典「诈尸」回归 / simplex-chat 私密通讯）；短龄高失衡 AI 投资·交易·视频·网关延续（OmniRoute 277:1 / ai-berkshire 260:1 / exercises-dataset 307:1 / Vibe-Trading 168:1）需谨慎；脚本继续全 19 项误标 NEW 已人工校正（真 NEW 8，RE 4：strix/supervision/superpowers/lingbot-map）
- [2026-06-30](daily/2026-06-30-analysis) — 安全·隐私工具集中同框是今日最清晰的结构信号（simplex-chat 守榜首 / maigret OSINT 回归 / VeraCrypt 磁盘加密首入 / VulnClaw AI 渗透 agent 新上榜）；认证基础设施 logto（OIDC + OAuth 2.1，自托管 Auth0 替代，信源强）是今日 grounding 最扎实的真 NEW；AI 投资·交易·决策 agent 延续短龄高失衡（ai-berkshire 313:1 / council-of-high-intelligence 173:1 / Vibe-Trading 170:1 / video-use 186:1 / FluidVoice 377:1）需谨慎；脚本继续全 15 项误标 NEW 已人工校正（真 NEW 仅 4，RE 3：agency-agents/maigret/tolaria）
- [2026-06-29](daily/2026-06-29-analysis) — 成熟知名开源项目集中回流是今日主轴（simplex-chat 隐私通讯 / free-for-dev 12.5万 / openpilot / cupy / system-design-101 / MinerU 六个重量级老项目同框）；AI 安全 agent strix（开源渗透测试，Show HN 102 分）+ 蚂蚁 lingbot-map（流式 3D 重建基础模型，arXiv + issue 技术讨论）是非知名 NEW 里 grounding 最扎实的；AI 投资·交易·视频 agent（video-use 176:1 零讨论且 6 周停更 / Vibe-Trading 160:1 / FluidVoice 377:1 乞 star / ai-berkshire 387:1）短龄高失衡需谨慎；脚本继续全 13 项误标 NEW 已人工校正（codebase-memory-mcp RE / ai-berkshire ↓1 / MinerU ↑4）
- [2026-06-26](daily/2026-06-26-analysis) — 成熟开源工具集中回流（MinerU 69K / CasaOS 34K / MediaCrawler 52K 三个长期项目同日首入 tracker），Claude Code/agent skills 生态继续占约半数（design.md 10→1 领涨、gstack/claude-code-best-practice/Anthropic 安全 skills/AWS 官方 agent-toolkit 同框）；阿里 page-agent 是今日 grounding 最扎实真信号（页面内 GUI agent，Show HN 147 分 76 评论，inside-out 范式）；TREK 481:1 / ai-berkshire 397:1 / open-seo 134:1 等短龄项目 stars/watchers 极端失衡且缺独立讨论需谨慎；脚本连续第三日全 16 项误标 NEW 已人工校正
- [2026-06-25](daily/2026-06-25-analysis) — coding-agent 工具继续主导榜单（约 8/13：OpenMontage/orca/design.md/no-mistakes/harness 等），但今日两个非 agent 项目 grounding 最扎实：apple/container（Apple 官方 Mac 跑 Linux 容器，RE 重新上榜）+ zapret-discord-youtube（俄区绕 DPI 封锁，issue #5704 720 条真实求助）；一批厂商主导短龄 agent 项目集中首入且 stars/subs 极端失衡（hiring-agent 558:1、no-mistakes 547:1、orca 456:1、design.md 163:1），传播靠厂商自有渠道、HN/Reddit 无独立讨论，需结合社区足迹判断；抓取脚本连续第二日把全部 13 项误标 NEW，已人工校正
- [2026-06-24](daily/2026-06-24-analysis) — agent skills / harness 生态全面霸榜（9/16），Anthropic 官方 plugins 目录 claude-plugins-official 首次成为权威锚点（平台方对第三方 skills 赛道做官方收口）；今天是存量轮动日，16/16 全为历史已上榜项目、零真新面孔；多个短龄 agent 项目 star/watchers 失衡（ECC 197:1、worldmonitor 162:1、gstack 166:1），daily_stock_analysis fork:star≈0.9:1 template 复制模式需结合社区足迹判断
- [2026-06-23](daily/2026-06-23-analysis) — AI 视频/创作工具仍占榜首梯队（OpenMontage/palmier-pro 单日增量领跑，新面孔 hyperframes 主打 HTML 渲染视频），但今日最扎实的真信号是成熟开源工具首入 tracker（firecrawl 137K/Stirling-PDF 83K/airllm）+ Claude Code 工具链回潮（gstack/mattpocock-skills/codebase-memory-mcp）；hyperframes(366:1 厂商主导)、ai-website-cloner-template(198:1 template 复制)等短龄高比值仓需区分成因解读
- [2026-06-22](daily/2026-06-22-analysis) — AI 创作/视频与「agent 记忆·上下文·代码智能」基础设施工具占榜单大半（headroom/codebase-memory-mcp/cognee/mattpocock-skills），成熟安全/设计工具集体回流（spiderfoot/penpot/Anthropic-Cybersecurity-Skills）；3 个真 NEW 中 spiderfoot（14 岁老牌 OSINT、商业版被 Intel 471 收购）与 biliTickerBuy（B 站抢票、中文社区扎实）grounding 最强，cognee 热度与社区足迹有落差；榜单 7/16 为 RE 回流，单日高增速需结合社区足迹判断
- [2026-06-20](daily/2026-06-20-analysis) — 周末榜单由「AI 创作/视频工具」与「成熟开源 SaaS 替代品回流」两条线主导：palmier-pro/OpenMontage/voicebox 撑起创作赛道，penpot/insomnia/twenty 集体回潮；turso、Pake、SmsForwarder 三个工具型项目首入 tracker，grounding 都偏扎实；palmier-pro/OpenMontage/headroom 等短龄高增速 AI 项目需结合社区足迹判断
- [2026-06-19](daily/2026-06-19-analysis) — 开源模型真发版（GLM-5.2 / LTX-2）与 AI 编码 agent 工具同框；GLM-5（HN 多帖高分 + Artificial Analysis 开源权重榜首 + MIT）与 LTX-2（19B 音视频联合生成、单卡可跑、评测 top-3）是今日 grounding 最扎实的真信号；palmier-pro/agent-native/codebase-memory-mcp 等短龄 agent 工具高比值、营销驱动需谨慎解读
- [2026-06-18](daily/2026-06-18-analysis) — AI agent/skills 框架强势回潮（superpowers +1,129 / mattpocock/skills +1,523 / codebase-memory-mcp NEW #1 同框），与近期"去 agent 化"形成反转；成熟开源 SaaS 替代品集体回流（RocketChat/chatwoot/plane/penpot/continue）；真信号最高的是 rlm（MIT 论文 + HN 多帖 + Prime Intellect 采用）与 iroh（1.0 余热 ↑11 升 #2）；Agent-Reach/OpenMontage/codebase-memory-mcp 三个高 ratio 短龄仓需结合 grounding 谨慎解读
- [2026-06-17](daily/2026-06-17-analysis) — 去 agent 化最彻底一天，agent 本体挂零；开发/测试工具（swc/puppeteer/cypress/meshery）+ 自托管/隐私集群（iptv-org/music-assistant/teslamate/OpenWA/UAD-NG）+ 真发版事件三类瓜分全榜；iroh 1.0 是唯一真实事件驱动（HN 1,351 分 + Holochain/Fedimint 真采用）；alibaba/zvec 嵌入式向量库 NEW；多数老牌工具今日 stars 个位/十位数属算法波动回流
- [2026-06-16](daily/2026-06-16-analysis) — 自托管 / 教育 / Windows 优化三条非 AI 赛道集体霸榜，去 agent 化延续；5 个真 NEW（teslamate / hello-algo / Win11Debloat / Self-Hosting-Guide / optimizerDuck）无一落在 agent 赛道；IPTV 双仓再次同框（iptv-org 重回 #1 +2,657 + Free-TV/IPTV）；真 AI 仅剩 SkillSpector（+1,079）与 cua 撑场；多数项目今日 stars 个位/十位数属 trending 算法波动回流
- [2026-06-15](daily/2026-06-15-analysis) — 成熟开发/测试工具集体回流主导榜单（pytest/swc/cypress/puppeteer/meshery/chatwoot/freeCodeCamp 同日同框），去 agent 化延续，真 AI 仅剩 SkillSpector + 定位漂移的 aisuite；IPTV 双仓同框（iptv-org #1 + Free-TV/IPTV）；多数回流项目今日 stars 仅个位/十位数，是 trending 算法波动而非真实增量
- [2026-06-13](daily/2026-06-13-analysis) — 榜单明显去 agent 化，三个真 NEW 全在 skill 赛道之外（music-assistant 自托管媒体 / iptv-org IPTV / LMCache LLM 推理缓存）；LMCache 被 NVIDIA Dynamo/Red Hat llm-d/字节 AIBrix/vLLM 同时采纳，是靠生产集成而非传播上榜的真采用样本；mattermost ↑15、PowerToys RE、apple/container +3,504 增量第一，成熟基础设施集体回流
- [2026-06-12](daily/2026-06-12-analysis) — apple/container ↑16 跃居榜首（+2,430），agent 生态长出"安全扫描 + 会话度量"二阶工具层（NVIDIA SkillSpector + Wes McKinney agentsview），4 个真 NEW 之外 restic/chatwoot/mattermost/fanqiang 四个知名老项目借发版集体首入 tracker
- [2026-06-11](daily/2026-06-11-analysis) — Apple 官方容器工具携 1.0 正式版 + WWDC26 双触发首入榜单（HN 1,197 分头条），agent/skill 板块强势回流，3 个 NEW 横跨系统容器、抗审查网络、agent 共享记忆三个方向
- [2026-06-10](daily/2026-06-10-analysis) — 榜单首次明显"去 agent 化"分流：计算机视觉双仓同框（supervision ↑9 + opencv RE）+ 边缘感知（espectre WiFi CSI 隔空人体检测，HN 215 分/Espressif 背书）+ 医疗 AI（openmed 本地 NER，HF 近 3000 万次下载）三方向同日浮现，3 个真 NEW 全部落在 agent 赛道之外；agent/skill 板块转入回流盘整（addyosmani/AiToEarn 回流，pm-skills/career-ops/openai 排名回落，last30days 仍 +3,191 守榜首）；解读提醒：工具仓/资料仓高 stars/subs 比值要看 GitHub 之外的真实足迹
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
