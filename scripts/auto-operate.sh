#!/bin/bash
# AI Daily Pulse - 全自动变现系统启动脚本
# 用途：一键启动所有自动化运营任务

echo "=========================================="
echo "AI Daily Pulse - 全自动变现系统"
echo "=========================================="
echo ""

# 1. 生成今日报告
echo "[1/4] 生成今日 AI 情报报告..."
cd /home/xiaosu/AI-Daily-Pulse
python3 scripts/generate_report.py
echo "✅ 报告生成完成"
echo ""

# 2. 生成小红书笔记
echo "[2/4] 生成小红书笔记..."
python3 scripts/xiaohongshu_auto_post.py
echo "✅ 笔记生成完成"
echo ""

# 3. 生成闲鱼商品
echo "[3/4] 生成闲鱼商品..."
python3 scripts/xianyu_auto_post.py
echo "✅ 商品生成完成"
echo ""

# 4. 推送到 GitHub
echo "[4/4] 推送到 GitHub..."
cd /home/xiaosu/AI-Daily-Pulse
git add .
git commit -m "Daily auto-update: $(date +%Y-%m-%d)"
git push origin main
echo "✅ GitHub 推送完成"
echo ""

echo "=========================================="
echo "全部完成！"
echo "=========================================="
echo ""
echo "已生成："
echo "- GitHub 报告：reports/$(date +%Y-%m-%d)-cn.md"
echo "- 小红书笔记：xiaohongshu_notes/"
echo "- 闲鱼商品：xianyu_products/"
echo ""
echo "下一步："
echo "1. 检查小红书笔记，复制发布"
echo "2. 检查闲鱼商品，复制发布"
echo "3. 等待用户咨询"
echo ""
