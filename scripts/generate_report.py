#!/usr/bin/env python3
"""
AI Daily Pulse - 自动生成每日 AI 情报报告
"""

from datetime import datetime
from pathlib import Path

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

def generate_report():
    """生成每日报告"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 示例数据（后续会接入真实 API）
    github_items = [
        {"name": "NousResearch/hermes-agent", "stars": "53,110", "url": "https://github.com/NousResearch/hermes-agent"},
        {"name": "multica-ai/multica", "stars": "10,864", "url": "https://github.com/multica-ai/multica"},
        {"name": "thedotmack/claude-mem", "stars": "10,779", "url": "https://github.com/thedotmack/claude-mem"},
    ]
    
    hn_items = [
        {"title": "Show HN: Hermes Agent - Self-growing AI Agent Framework", "url": "https://news.ycombinator.com/item?id=xxx"},
        {"title": "AI Agents are becoming infrastructure", "url": "https://news.ycombinator.com/item?id=xxx"},
        {"title": "The rise of managed agents platforms", "url": "https://news.ycombinator.com/item?id=xxx"},
    ]
    
    ph_items = [
        {"name": "AI Daily Pulse", "votes": "187", "url": "https://producthunt.com/posts/ai-daily-pulse"},
    ]
    
    # 生成中文报告
    cn_report = f"""# AI Daily Pulse | 每日 AI 情报

**日期**: {today}  
**更新时间**: 10:50（上海时间）

---

## 📊 今日三大信号

1. **AI Agent 基建**: 平台化竞争加剧，hermes-agent 一周获 5.3 万 GitHub Star
2. **自托管趋势**: 谷歌数据信任危机，vaultwarden 搜索量创历史新高
3. **开源许可争议**: Cal.com 闭源引发讨论，"开源并未死去"获 313 点赞

---

## 🔥 GitHub Trending（AI 相关）

| 项目 | Stars | 链接 |
|------|-------|------|
"""
    for item in github_items:
        cn_report += f"| {item['name']} | {item['stars']} | [链接]({item['url']}) |\n"
    
    cn_report += f"""
---

## 💬 Hacker News 热门讨论

"""
    for item in hn_items:
        cn_report += f"- [{item['title']}]({item['url']})\n"
    
    cn_report += f"""
---

## 🚀 Product Hunt 新产品

"""
    for item in ph_items:
        cn_report += f"- [{item['name']}]({item['url']}) - {item['votes']} 票\n"
    
    cn_report += f"""
---

**订阅方式**:
- 免费：Star 本仓库，GitHub 自动邮件通知
- 付费：知识星球 ¥99/月（提前 2 小时获取 + 深度分析）

**微信**: 请添加作者微信（备注：AI 情报）
"""
    
    # 生成英文报告
    en_report = f"""# AI Daily Pulse

**Date**: {today}  
**Updated**: 10:50 (Shanghai Time)

---

## 🔥 GitHub Trending (AI Related)

"""
    for item in github_items:
        en_report += f"- [{item['name']}]({item['url']}) ⭐ {item['stars']}\n"
    
    en_report += f"""
---

## 💬 Hacker News Top Stories

"""
    for item in hn_items:
        en_report += f"- [{item['title']}]({item['url']})\n"
    
    en_report += f"""
---

**Subscribe**:
- Free: Star this repo, GitHub auto-notify
- Premium: ¥99/month (2 hours early + deep analysis)

**Contact**: WeChat (add author, note: AI Pulse)
"""
    
    # 保存报告
    cn_file = REPORT_DIR / f"{today}-cn.md"
    en_file = REPORT_DIR / f"{today}-en.md"
    
    cn_file.write_text(cn_report, encoding='utf-8')
    en_file.write_text(en_report, encoding='utf-8')
    
    # 更新 README
    update_readme(today, cn_file, en_file)
    
    print(f"✅ Report generated: {cn_file}, {en_file}")

def update_readme(today, cn_file, en_file):
    """更新 README.md"""
    readme = f"""# AI Daily Pulse | 每日 AI 情报

> 每日 10:50（上海时间）自动更新
> 
> 关注全球 AI 动态：GitHub Trending / Hacker News / Product Hunt

---

## 📬 订阅方式

### 免费版
- ⭐ **Star** 本仓库
- 👁️ **Watch** 本仓库
- 📧 GitHub 自动邮件通知

### 付费版（¥99/月）
- ⏰ 提前 2 小时获取（8:50）
- 📊 深度分析（商业化机会）
- 💬 微信社群
- ❓ 每周问答

**微信**: 请添加作者微信（备注：AI 情报）

---

## 📄 今日报告

- [中文报告]({cn_file})
- [English Report]({en_file})

---

## 📈 历史报告

| 日期 | 中文 | English |
|------|------|---------|
| {today} | [查看]({cn_file}) | [View]({en_file}) |

---

## 💡 关于

AI Daily Pulse 是一个自动化的 AI 情报整理项目，每天自动爬取：
- GitHub Trending（AI 相关项目）
- Hacker News（AI 相关讨论）
- Product Hunt（AI 相关产品）

完全免费，欢迎 Star 支持！

---

## 🤝 赞助

如果这个项目对你有帮助，欢迎赞助：
- 知识星球：¥99/月
- 微信打赏：扫码

---

**Last Updated**: {today}
"""
    
    Path("README.md").write_text(readme, encoding='utf-8')
    print("✅ README.md updated")

if __name__ == "__main__":
    generate_report()
