#!/usr/bin/env python3
"""
闲鱼自动发布脚本
用途：自动生成商品并发布到闲鱼
"""

import json
from datetime import datetime
from pathlib import Path

# 商品模板库
PRODUCT_TEMPLATES = {
    "AI 情报订阅": {
        "标题": "AI 情报订阅 每日更新 GitHub/HN/PH 动态 免费版/付费版",
        "描述": """【服务内容】
✅ 每日 AI 情报报告
✅ GitHub Trending
✅ Hacker News 热门
✅ Product Hunt 新产品

【价格】
💰 免费版：GitHub 关注（免费）
💰 付费版：¥99/月（提前 2 小时 + 深度分析）

【交付方式】
免费版：GitHub 仓库自动更新
付费版：微信私发 + 知识星球

【更新时间】
每天 10:50（上海时间）

【适合谁】
- AI 从业者
- 独立开发者
- 创业者
- 对 AI 感兴趣的人

【订阅方式】
GitHub 搜索：AI-Daily-Pulse
Star + Watch，自动邮件通知

【付费版权益】
- 提前 2 小时获取（8:50）
- 深度分析（商业化机会）
- 微信社群
- 每周问答

微信：请私信获取（备注：AI 情报）
""",
        "分类": "服务 → 文案/写作",
        "价格": "99.00",
    },
    "AI 文案代写": {
        "标题": "AI 文案代写 小红书笔记 公众号文章 新店铺冲销量 9.9 元起 当天交付",
        "描述": """【新店铺冲销量！亏本赚吆喝！】

✅ 小红书笔记代写 ¥9.9/篇（原价¥99）
✅ 5 篇套餐 ¥39.9（原价¥450）
✅ 10 篇套餐 ¥69.9（原价¥850）

【为什么这么便宜？】
新店开业，需要好评和销量！
质量保证，不满意免费修改！
只求好评，不求赚钱！

【交付内容】
✅ 标题 5 个备选
✅ 正文 800-1500 字
✅ 标签 10-15 个
✅ 配图建议

【交付时间】
⏰ 当天交付（24 小时内）

【修改政策】
🔄 不满意免费修改，改到满意为止！

【温馨提示】
虚拟商品，不支持退款
但保证质量，修改到满意！

新店铺，求好评！🙏
""",
        "分类": "服务 → 文案/写作",
        "价格": "9.90",
    },
    "AI 简历优化": {
        "标题": "AI 简历优化 新店铺冲销量 29.9 元起 过 HR 筛选",
        "描述": """【新店铺冲销量！亏本赚吆喝！】

✅ 基础版 ¥29.9（原价¥199）
✅ 进阶版 ¥49.9（原价¥399）
✅ 全套版 ¥79.9（原价¥599）

【为什么这么便宜？】
新店开业，需要好评和销量！
质量保证，不满意免费修改！
只求好评，不求赚钱！

【交付内容】
✅ 简历内容优化
✅ 格式调整
✅ 关键词优化（过 HR 筛选）
✅ 修改建议

【交付时间】
⏰ 当天交付（24 小时内）

【修改政策】
🔄 不满意免费修改，改到满意为止！

新店铺，求好评！🙏
""",
        "分类": "服务 → 求职/招聘",
        "价格": "29.90",
    },
}

def generate_product(product_type="AI 情报订阅"):
    """生成闲鱼商品"""
    template = PRODUCT_TEMPLATES.get(product_type, PRODUCT_TEMPLATES["AI 情报订阅"])
    
    return {
        "title": template["标题"],
        "description": template["描述"],
        "category": template["分类"],
        "price": template["价格"],
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def save_product(product):
    """保存商品到本地"""
    output_dir = Path("xianyu_products")
    output_dir.mkdir(exist_ok=True)
    
    filename = output_dir / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(product, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Product saved: {filename}")
    return filename

if __name__ == "__main__":
    # 生成 3 个商品
    for product_type in ["AI 情报订阅", "AI 文案代写", "AI 简历优化"]:
        product = generate_product(product_type)
        print(f"\n📦 {product_type} 商品：")
        print(f"标题：{product['title'][:50]}...")
        print(f"价格：¥{product['price']}")
        save_product(product)
    
    print("\n✅ 商品生成完成！")
    print("下一步：用浏览器工具发布到闲鱼")
