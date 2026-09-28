# 使用 Codex 部署 / 测试本 Skill

## 1. 打开项目

解压后，在 Codex App / IDE 中打开整个：

`ecommerce-hero-visual-skill`

或者终端进入该目录后运行：

```bash
codex
```

## 2. 先让 Codex 检查项目

把下面这段发给 Codex：

```text
请检查当前仓库，这是一个 Codex repository-local Skill 项目。

请完成以下任务：
1. 检查 .agents/skills/ecommerce-hero-visual/SKILL.md 的 YAML front matter。
2. 检查 references 和 examples 文件是否都存在。
3. 检查是否存在重复、冲突或过度复杂的指令。
4. 保留以下原则：
   - 先分析再生成
   - 锁定商品真实性
   - 不编造商品事实
   - 优先生成无文字底图，再排版文字
   - 最终执行 QA 和迭代
5. 使用 NORI-test-case.md 做一次完整测试。
6. 如有必要，直接修改仓库文件。
7. 最后输出修改摘要和最终文件树。
暂时不要 git push。
```

## 3. 测试 Skill

```text
Use $ecommerce-hero-visual.

Read:
.agents/skills/ecommerce-hero-visual/examples/NORI-test-case.md

Output:
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

Do not invent facts.
```

## 4. 准备 GitHub 仓库

```text
请把当前项目整理成适合公开提交的 GitHub 课程作业仓库。

请：
1. 检查 README.md
2. 检查是否存在隐私信息、API key、密码或临时文件
3. 检查 .gitignore
4. 执行 git status
5. 如未初始化 Git，则初始化
6. 添加需要提交的文件
7. 创建第一次 commit

Commit message:
Initial ecommerce hero visual skill

完成后停止，不要 push。
```

## 5. 推送 GitHub

创建空 GitHub 仓库后，把仓库地址给 Codex，再输入：

```text
GitHub 仓库地址是：
<在这里粘贴你的仓库地址>

请：
1. 设置 origin
2. 检查 remote
3. push 当前分支
4. 不要 force push
5. 不要重写历史
```

如果 GitHub 尚未登录，请你自己先执行：

```bash
gh auth login
```

不要把 GitHub Token 直接粘贴到聊天里。
