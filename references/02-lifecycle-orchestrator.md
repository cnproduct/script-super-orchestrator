# 剧本全流程六阶段执行状态机 (Lifecycle Orchestrator)

在剧本创作过程中，**Script Super Orchestrator** 严格执行流水线化的工业标准。无论是 3 集精品短剧还是 100 集商业网剧，均按以下 6 个阶段有序推进。

---

## 阶段 1：选题立项与题材雷达 (Logline & Premise)

- **输入**：创作者的一个脑洞、灵感片段、小说 IP、或热门时事热点。
- **调度子技能**：
  - `short-drama/references/genre-guide.md`（题材定位）
  - `screenwriting-skills/plugins/screenwriting/skills/sw-premise-theme/`（核心前提与反前提）
  - `short-drama/references/compliance-checklist.md`（合规筛查）
- **阶段交付物**：
  1. **一句话 Logline**：【主角身份】在【突发危机】下，必须依靠【独特手段/金手指/手艺】，在【时限约束】内达成【终极目标】，否则将付出【毁灭性代价】。
  2. **核心哲学冲突 (Theme vs Counter-Theme)**：剧作探讨的本质价值对抗。
  3. **受众画像与卖点分析**。
- **质量闸口 (Gate 1)**：题材是否具有足够的情绪烈度与现实痛点？是否存在平台合规风险？

---

## 阶段 2：故事骨架与人物小传 (Bible & Arc)

- **输入**：通过 Gate 1 的 Logline 与题材方向。
- **调度子技能**：
  - `screenwriting-skills/plugins/screenwriting/skills/sw-truby-anatomy/`（特鲁比 22 步故事线）
  - `short-drama/references/villain-design.md`（四层反派体系）
  - `screenwriting-skills/plugins/screenwriting/skills/sw-character-conflict/`（人物冲突动力学）
- **阶段交付物**：
  1. **主角人物卡**：心理创伤 (Ghost) + 表面欲求 (Want) + 真正内在需要 (Need) + 救赎时刻。
  2. **对立面反派矩阵**：每位对手的动机合理性（拒绝降智扁平）。
  3. **全剧核心七大节拍点**：起因 → 触发事件 → 第一幕转折 → 中点危机 → 黑暗绝望之夜 → 决战高潮 → 终局余韵。
- **质量闸口 (Gate 2)**：主角是否有致命弱点？人物行动是否由欲望驱动而非作者生硬推动？

---

## 阶段 3：分集大纲与心电图卡点 (Beat Sheet & Hooks)

- **输入**：人物小传与核心故事骨架。
- **调度子技能**：
  - `short-drama/references/opening-rules.md`（黄金前 3 秒起爆法则）
  - `short-drama/references/hook-design.md`（5 大集尾断章钩子）
  - `short-drama/references/rhythm-curve.md` & `paywall-design.md`（心电图与付费卡点）
- **阶段交付物**：
  1. **分集节拍表 (Beat Sheet)**：每集明确标出【前3秒Hook】、【中段转折】、【集尾断章悬念】。
  2. **付费卡点规划**：在关键集数（如微短剧第 8-12 集）埋设最大信息差曝光或身份揭晓爆点。
- **质量闸口 (Gate 3)**：每集结尾是否留有“不得不看下一集”的强烈悬念？是否有超过两集平淡无冲突？

---

## 阶段 4：逐场剧本创作与潜台词锤炼 (Scene Craft & Subtext)

- **输入**：确定好的分集大纲。
- **调度子技能**：
  - `screenwriting-skills/plugins/screenwriting/skills/sw-dialogue/`（潜台词三层剥离法）
  - `screenwriting-skills/plugins/screenwriting/skills/sw-scene-craft/`（单场戏价值正负翻转）
  - `zenstory-drama-skills/skills/short-drama-write/references/scene-sound-dramaturgy.md`（声音戏剧学）
- **阶段交付物**：
  1. **标准分场剧本**（包含：场号、时间、地点、人物、△动作描写、♪声音音效、人物台词）。
  2. **潜台词校验批注**：剔除直白说明性台词，用动作与微表情支撑戏剧张力。
- **质量闸口 (Gate 4)**：入场情绪与出场情绪是否发生有效位移？台词是否言之有物、个性鲜明？

---

## 阶段 5：主编级审稿质检与反套路去 AI 味 (Review & Iron Rules)

- **输入**：初稿剧本文本。
- **调度子技能**：
  - `screenwriter-skill/references/iron_rules.md`（37 条毒舌审稿铁律）
  - `zenstory-drama-skills/skills/short-drama-review/references/anti-template-repair.md`（去 AI 味套路清洗）
- **阶段交付物**：
  1. **量化审稿评级报告**：评定 S+ / S / A / B / C 五档等级。
  2. **毒舌问题清单**：按“人物动机 / 情节逻辑 / 对白去水 / 节奏卡点 / 平台合规”五维度开出药方。
  3. **一键精修改稿版**。
- **质量闸口 (Gate 5)**：评级必须达到 S 级以上方可进入分镜出片阶段。

---

## 阶段 6：视听分镜转译与 AI 出片规约 (Storyboard & Prompts)

- **输入**：定稿剧本。
- **调度子技能**：
  - `seedance-screenwriter/.claude/skills/screenwriter/references/`（镜头、光位、构图、风格）
  - `ai-drama-craftsman`（零字幕底片规范 + 张嘴口型控制 + 物理动量因果锁）
  - `zenstory-drama-skills/skills/short-drama-video-prompts/references/seedance-2.0.md`
- **阶段交付物**：
  1. **导演分镜台本**：景别、机位移动、演员走位、Foley 拟音对轨。
  2. **AI 视频生成提示词包**：100% 干净无台词黑条、带有动作闭环与物理重力逻辑的纯英文/中英双语生成词。
- **质量闸口 (Gate 6)**：提示词是否消除了违和伸手与悬空漂浮？是否符合 Seedance 2.0 Fast / 2.5 竖屏标准？
