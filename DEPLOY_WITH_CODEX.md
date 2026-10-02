# 使用 Codex 测试 Ecommerce Hero Visual Skill V2

## 1. 打开项目

在 Codex App 或 IDE 中打开整个 ecommerce-hero-visual-skill 项目目录。

Skill 入口：

.agents/skills/ecommerce-hero-visual/SKILL.md

## 2. V2 核心输入

V2 使用五类 Reference Asset：

- Product Reference Image，ID 前缀 PR；
- Product Detail Reference，ID 前缀 PD；
- Brand Asset，ID 前缀 BA；
- Style Reference，ID 前缀 SR；
- Layout Reference，ID 前缀 LR。

向 Codex 提供图片时，应说明图片属于哪一类、来源是否获批，以及允许用途。如果用户没有指定，Skill 应先分类并建立 Reference Asset Inventory。

Layout Reference 只允许影响 composition、information density、visual hierarchy、text/product balance 和 negative-space planning。它不能改变商品形状、颜色、材质、Logo、功能、配件或事实，也不能要求复制参考设计本身。

## 3. 实际素材输入接口

仓库素材入口位于：

- inputs/product-images/
- inputs/brand-assets/
- inputs/style-references/
- inputs/layout-references/
- input-manifest.yaml，如果当前任务已从 example 模板复制并填写

也可以直接向 Codex 上传图片，不要求所有素材必须存入仓库。两种输入方式最终都必须进入同一个 Reference Asset Inventory。

实际测试提示词：

~~~text
Use $ecommerce-hero-visual.

Inspect:

- input-manifest.yaml if present
- all relevant images in inputs/

First create:

1. Reference Asset Inventory
2. Product Reference Analysis
3. Product Fidelity Lock

Then continue the full workflow.

Do not start final fidelity-sensitive generation unless at least one valid Product Reference Image exists.
~~~

input-manifest.example.yaml 只是模板。只有实际存在的仓库文件或用户直接上传的附件才能进入 Reference Asset Inventory。

## 4. 两种生产模式

### Reference-backed Fidelity Mode

至少需要一张可用、获批的 Product Reference Image。该模式可以进入商品分析、Fidelity Lock、参考图生产和 Side-by-side Reference QA。

### Planning-only Mode

没有可用 Product Reference Image 时使用。可以完成策略、方向、版式、Prompt 和文案规划，但不得生成或声称完成最终保真商品视觉。

## 5. 运行 NORI 负向测试

向 Codex 输入：

~~~text
Use ecommerce-hero-visual.

Read:
.agents/skills/ecommerce-hero-visual/examples/NORI-test-case.md

Execute the full V2 workflow. Do not invent reference assets or product appearance.
~~~

预期结果：

- Reference Asset Inventory 中没有虚构资产；
- 选择 Planning-only Mode；
- Product Reference Analysis 和 Product Fidelity Lock 为 Blocked；
- 可以完成策略和文案规划；
- 所有方向的最终执行 Reference Feasibility 为 Blocked；
- 最终商品生成和 Side-by-side Reference QA 保持 Blocked。

## 6. 准备未来的正向测试

阅读：

.agents/skills/ecommerce-hero-visual/examples/reference-backed-test-spec.md

正向测试至少需要真实、获准使用的 PR-01。需要展示局部结构时，再提供 PD-01。如果最终图需要 Logo，应提供官方 BA-01。

SR-01 和 LR-01 为可选资产。即使它们包含其他商品、Logo、价格或文案，也只能使用各自获准的风格或版式属性。

本仓库当前不包含合法商品图片 fixture。不要生成一张假商品图冒充真实参考图，也不要把模型生成图作为商品真实性来源。

## 7. 推荐的正向生产方式

1. 建立 Reference Asset Inventory；
2. 完成 Product Reference Analysis；
3. 建立可追溯到 Reference ID 的 Product Fidelity Lock；
4. 为每个视觉方向评估 Reference Feasibility 和 Fidelity Risk；
5. 建立 Reference Image Usage Plan；
6. 单独生成无商品、无文字的背景；
7. 使用获批商品抠图或原始商品像素进行合成；
8. 检查商品保真和负空间；
9. 直接放置官方 Brand Asset；
10. 添加确认文案；
11. 执行 Side-by-side Reference QA；
12. 修复 Blocking 和 High 问题后重新检查。

只有在工具和参考图适合、且商品身份可以验证时，才使用 reference-guided generation。禁止仅凭商品名称和文字描述重建真实商品。

## 8. 验证 Skill

项目本身没有自定义验证脚本。如果本机提供 Codex Skill Creator 的 quick_validate.py，可以对以下目录运行：

.agents/skills/ecommerce-hero-visual/

此外应检查：

- SKILL.md YAML front matter；
- 所有 Markdown 相对链接；
- references 和 examples 文件存在；
- NORI 负向测试行为；
- 正向测试规范没有假图片；
- SR 和 LR 权限边界；
- 最终 QA 是否真正引用 PR、PD 和 BA。

## 9. Git 检查

修改后先运行 git status 和 git diff，不要直接覆盖 V1 基线。确认变更只位于 feature/product-reference-input 分支后再决定是否提交。

公开提交前再次检查仓库中是否存在私有商品图、客户素材、API key、密码、Token 或无权发布的 Brand Asset。
