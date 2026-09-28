# Ecommerce Hero Visual Skill

一个 Codex repository-local Skill，用于规划和制作电商商品营销主视觉、活动海报、商品主图和双语产品 Key Visual。

## 项目目的

本 Skill 将商品图片、已确认的商品事实、卖点、活动信息、品牌规范和画布要求，整理为：

1. 结构化任务简报
2. 信息传播层级
3. 视觉方向和推荐方案
4. 版式蓝图
5. 无文字底图生成 Prompt
6. 中文和英文文案规划
7. QA 检查、问题修正和复查结果

它遵循以下原则：

- 先分析需求和证据，再生成视觉；
- 将商品图片和已确认事实作为真实性来源；
- 不编造或升级商品参数、功能、价格、折扣、日期、认证、奖项、促销规则或 Logo；
- 优先生成无文字视觉底图，再独立完成文字排版；
- QA 发现阻塞问题时，标记为 Blocked，不把未完成结果称为最终交付。

## 目录结构

项目包含 .agents/skills/ecommerce-hero-visual/，其中有主 Skill 文件、NORI 测试案例、测试结果记录和四份 references。

## 使用方法

在 Codex 中打开本项目根目录，然后要求使用 $ecommerce-hero-visual，读取：

.agents/skills/ecommerce-hero-visual/examples/NORI-test-case.md

并输出：

1. Structured Brief
2. Missing Information
3. Communication Hierarchy
4. Three Visual Directions
5. Recommended Direction
6. Layout Blueprint
7. Text-free Generation Prompt
8. Chinese Copy Plan
9. English Copy Plan
10. QA Checklist

同时明确：Do not invent product facts.

也可以把同样的工作流用于新的商品 Brief。需要最终商品视觉时，应同时提供已批准的商品参考图、官方 Logo 和相关品牌规范。

## 测试案例

测试案例位于：

.agents/skills/ecommerce-hero-visual/examples/NORI-test-case.md

预期测试结果记录位于：

.agents/skills/ecommerce-hero-visual/examples/NORI-test-result.md

NORI 案例故意不包含商品参考图。正确行为是完成策略、文案和预检 QA，同时将最终商品图生成与商品真实性 QA 标记为 Blocked，而不是编造商品外观。

## 验证

Skill 的 YAML front matter 和目录结构可使用 Codex Skill Creator 的 quick_validate.py 检查。当前 Skill 已通过该验证。

本仓库只包含 Skill 指令、参考文档和测试材料，不包含 API key、密码、商品私有素材或生成后的临时文件。
