#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Super Orchestrator - Dispatch Inspector
根据输入的题材主题与创作阶段，快速查询匹配的子技能与知识库文档。
"""

import sys
import json

THEME_DISPATCH = {
    "life": {
        "name": "市井生活流 / 温情治愈",
        "skills": ["screenwriting-skills/ozu-screenplay-style", "zenstory-drama-skills/short-drama-write", "screenwriting-skills/sw-scene-craft"],
        "references": ["01-theme-genre-matrix.md", "scene-sound-dramaturgy.md", "anti-template-repair.md"],
        "core_principle": "器物赋灵叙事，声音戏剧学替代心理直白描写，生活流留白。"
    },
    "revenge": {
        "name": "都市逆袭 / 商业爽剧",
        "skills": ["short-drama", "screenwriter-skill", "drama-trend-rewriter"],
        "references": ["opening-rules.md", "satisfaction-matrix.md", "villain-design.md", "hook-design.md"],
        "core_principle": "前3秒起爆，四层递进反派，1:2.5憋屈与打脸爽感释放矩阵。"
    },
    "suspense": {
        "name": "悬疑反转 / 犯罪推理",
        "skills": ["short-drama/hook-design", "screenwriting-skills/sw-truby-anatomy"],
        "references": ["hook-design.md", "sw-truby-anatomy/reference.md"],
        "core_principle": "信息差钩，倒计时危机压迫，伏笔精准闭环回收。"
    },
    "drama": {
        "name": "多线权谋 / 家族职场博弈",
        "skills": ["screenwriting-skills/succession-series-writing", "screenwriting-skills/sw-dialogue"],
        "references": ["succession-series-writing/reference.md", "sw-dialogue/reference.md"],
        "core_principle": "群像位阶流动，潜台词Subtext攻防，表面体面内里刀光剑影。"
    }
}

STAGE_DISPATCH = {
    "1": ("选题立项", ["short-drama/genre-guide", "sw-premise-theme"], "Logline与核心哲学对抗"),
    "2": ("人物大纲", ["sw-truby-anatomy", "short-drama/villain-design"], "人物小传三要素与故事节拍"),
    "3": ("分集卡点", ["short-drama/opening-rules", "short-drama/hook-design"], "前3秒Hook与集尾断章钩子"),
    "4": ("分场正文", ["sw-dialogue", "sw-scene-craft", "zenstory-drama-skills/dialogue-craft"], "单场价值翻转与潜台词去说明化"),
    "5": ("审稿质检", ["screenwriter-skill/iron_rules", "zenstory-drama-skills/anti-template-repair"], "37条铁律排查与去AI味量化打分"),
    "6": ("视听出片", ["seedance-screenwriter", "ai-drama-craftsman"], "Seedance提示词与零字幕口型规范")
}

def inspect(theme_key="life", stage_key="4"):
    theme_info = THEME_DISPATCH.get(theme_key, THEME_DISPATCH["life"])
    stage_info = STAGE_DISPATCH.get(stage_key, STAGE_DISPATCH["4"])
    
    report = {
        "theme": theme_info["name"],
        "core_principle": theme_info["core_principle"],
        "recommended_theme_skills": theme_info["skills"],
        "current_stage": stage_info[0],
        "stage_skills": stage_info[1],
        "stage_deliverable": stage_info[2]
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    t = sys.argv[1] if len(sys.argv) > 1 else "life"
    s = sys.argv[2] if len(sys.argv) > 2 else "4"
    inspect(t, s)
