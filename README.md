# 🎭 Script Super Orchestrator (全流程剧本智造总控引擎)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agent Skills Standard](https://img.shields.io/badge/Standard-AgentSkills.io-blue)](https://agentskills.io)
[![Multi-Agent Ready](https://img.shields.io/badge/Multi--Agent-Ready-green.svg)]()

> **Full-Lifecycle Script & Screenplay Super Orchestrator Agent Skill.**  
> 统筹调度 5 大底层知识库集群与 40+ 专项剧作子技能，根据剧本题材（生活流/爽剧/悬疑/博弈）与创作阶段（立项/人设/大纲/对白/审稿/视听出片），自适应分配行业最佳实践知识库。

---

## 🌟 核心特性 (Key Features)

1. **五大知识库集群全景整合**：
   - **商业微短剧爆款库 (`short-drama`)**：黄金前 3 秒起爆、5 大集尾断章钩子、四层递进反派体系、1:2.5 爽感压强公式。
   - **学院派经典剧作体系 (`screenwriting-skills`)**：约翰·特鲁比 22 步故事解剖学、潜台词 (Subtext) 艺术、小津生活流留白、契诃夫潜流戏剧。
   - **短剧工业全流程 (`zenstory-drama-skills`)**：声音戏剧学（动作拟音替代旁白）、反套路去 AI 味修复指南、全题材评测集。
   - **主编级毒舌审稿库 (`screenwriter-skill`)**：37 条实战审稿铁律、S+ 至 C 级量化评审打分、处方级改稿手术方案。
   - **Seedance 视听编剧专项 (`seedance-screenwriter & ai-drama-craftsman`)**：运镜机位、侧向体积切光、深焦透视、零字幕底片规约与张嘴口型控制。

2. **主题与题材智能调度矩阵**：
   - 根据输入题材（市井温情生活流、都市逆袭、家族权谋、悬疑推理），一键挂载对应剧作法。

3. **六阶段流水线执行状态机**：
   - `Stage 1: 选题立项` ➔ `Stage 2: 人设骨架` ➔ `Stage 3: 分集卡点` ➔ `Stage 4: 分场潜台词` ➔ `Stage 5: 审稿质检` ➔ `Stage 6: 视听出片`。

---

## 📂 仓库目录结构 (Architecture)

```text
script-super-orchestrator/
├── SKILL.md                          # 总控 Skill 核心入口与指令逻辑
├── README.md                         # 综合文档
├── LICENSE                           # MIT 协议
├── references/                       # 核心总控知识库
│   ├── 01-theme-genre-matrix.md      # 主题与题材智能调度矩阵
│   ├── 02-lifecycle-orchestrator.md  # 创作六阶段状态机与质量闸口
│   ├── 03-subskills-dispatch-map.md  # 全部涵盖子技能与知识库物理映射
│   └── 04-iron-rules-and-anti-ai.md  # 37条审稿铁律与去AI味核心准则
├── templates/                        # 工业级剧本输出模板
│   ├── 01-character-bible-template.md# 人物小传与角色网络卡
│   ├── 02-episode-outline-template.md# 分集大纲与节拍卡点表
│   ├── 03-scene-script-template.md   # 标准分场剧本模板
│   └── 04-review-report-template.md  # 审稿诊断报告模板
└── scripts/
    └── dispatch_inspector.py         # 智能调度检测辅助脚本
```

---

## 🚀 快捷调用指令 (Quick Slash Commands)

| 指令 | 目标阶段 | 说明与产出 |
| :--- | :--- | :--- |
| `/plan [题材/脑洞]` | 阶段 1 & 2 | 主题分类判定、核心哲学冲突、主角弧光三要素与人物小传卡 |
| `/outline [集数]` | 阶段 3 | 输出带前 3 秒黄金 Hook、集尾 5 类断章钩子的分集节拍表 |
| `/write [集号/场次]` | 阶段 4 | 运用潜台词与声音戏剧学编写正文剧本，严禁说明性台词 |
| `/review [剧本文本]` | 阶段 5 | 启动 37 条审稿铁律逐项诊断，出具 S+～C 级评审打分报告 |
| `/prompt [分镜画面]` | 阶段 6 | 转化为符合 Seedance 2.0 Fast / 2.5 竖屏规范的工业级提示词 |

---

## 📦 安装与配置 (Installation)

克隆至你的 Agent Skills 目录：

```bash
# 适用于 Antigravity, Claude Code, Cursor 等
git clone https://github.com/cnproduct/script-super-orchestrator.git .agents/skills/script-super-orchestrator
```

---

## 📄 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源协议。
