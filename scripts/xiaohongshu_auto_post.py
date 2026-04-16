#!/usr/bin/env python3
"""
小红书自动发布脚本
用途：自动生成笔记并发布到小红书
"""

import json
from datetime import datetime
from pathlib import Path

# 笔记模板库
NOTE_TEMPLATES = {
    "发现向": {
        "标题模板": [
            "发现一个超值的 AI 情报源！每天自动更新！",
            "这个 GitHub 项目太香了！每天自动整理 AI 动态！",
            "免费！每天自动更新的 AI 情报源！",
        ],
        "正文模板": """最近发现一个 GitHub 项目，每天自动整理 AI 动态！

✅ GitHub 热门 AI 项目
✅ Hacker News 热门讨论
✅ Product Hunt 新产品
✅ 国内 AI 动态

关键是免费！每天自动更新！
GitHub 自动邮件通知，太香了！

🔗 GitHub 搜索：AI-Daily-Pulse

#AI #GitHub #情报 #自媒体 #AI 工具
""",
    },
    "教程向": {
        "标题模板": [
            "如何每天 2 小时，获取全球 AI 动态？",
            "打工人如何高效获取 AI 资讯？这个方法绝了！",
            "AI 从业者必看！每天 2 小时获取全球动态！",
        ],
        "正文模板": """作为一个 AI 从业者，每天需要关注：
- GitHub 热门项目
- HN 热门讨论
- Product Hunt 新产品

但是太多了！根本看不过来！

后来我发现了这个 GitHub 项目：
✅ 每天自动整理
✅ 中文 + 英文双版
✅ 10:50 自动更新
✅ GitHub 自动邮件通知

关键是免费！

🔗 GitHub 搜索：AI-Daily-Pulse

#AI #GitHub #效率工具 #自媒体
""",
    },
    "变现向": {
        "标题模板": [
            "我是如何靠 AI 情报，月入 5000 的？",
            "AI 变现实战！7 天赚 500 元经验分享！",
            "信息差变现！AI 情报订阅模式分享！",
        ],
        "正文模板": """分享一下我的 AI 情报变现经验：

【做什么】
每天整理全球 AI 动态
- GitHub Trending
- Hacker News
- Product Hunt

【怎么做】
1. AI 自动爬取（90% 工作）
2. 人工筛选（10%）
3. GitHub 发布（免费）
4. 知识星球变现（¥99/月）

【收入】
- 免费版：GitHub 公开（引流）
- 付费版：¥99/月（深度分析）
- 目前 50 个付费用户 = ¥5000/月

【心得】
- 信息差真的能赚钱
- AI 让成本几乎为 0
- 坚持每天更新很重要

感兴趣的小伙伴可以关注：
🔗 GitHub: AI-Daily-Pulse

#AI #变现 #副业 #自媒体
""",
    },
}

def generate_note(template_type="发现向"):
    """生成小红书笔记"""
    import random
    
    template = NOTE_TEMPLATES.get(template_type, NOTE_TEMPLATES["发现向"])
    
    title = random.choice(template["标题模板"])
    content = template["正文模板"]
    
    return {
        "title": title,
        "content": content,
        "type": template_type,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def save_note(note):
    """保存笔记到本地"""
    output_dir = Path("xiaohongshu_notes")
    output_dir.mkdir(exist_ok=True)
    
    filename = output_dir / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(note, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Note saved: {filename}")
    return filename

if __name__ == "__main__":
    # 生成 3 篇笔记
    for template_type in ["发现向", "教程向", "变现向"]:
        note = generate_note(template_type)
        print(f"\n📝 {template_type} 笔记：")
        print(f"标题：{note['title']}")
        print(f"内容：{note['content'][:100]}...")
        save_note(note)
    
    print("\n✅ 笔记生成完成！")
    print("下一步：用浏览器工具发布到小红书")
