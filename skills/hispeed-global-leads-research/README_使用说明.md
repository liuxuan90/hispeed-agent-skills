# 乐速海外客户开发 Skill — 试运行说明

**当前状态：V1.0 待发布至私有仓库；Snov.io、Google Sheets、企业微信、Muse 的实际授权与端到端执行尚未接通。**

## 为什么是这个结构
- 固定入口 `SKILL.md`：规定流程、边界、更新脚本调用。
- `references/*.md`：可长期更新的业务规则，GitHub 发布后自动同步至本地。
- `scripts/update_rules.py`：只下载经过 SHA256 对照的 Markdown 文件，不下载或执行任意远端 Python 脚本。
- `rules-manifest.json`：规则版本及文件哈希。
- `config/update.json`：第一次发布到私有 GitHub 时填入仓库名、稳定分支等。
- `assets/sheets/*.csv`：四张工作表字段模板。

## 1. 在 GitHub 建立私有仓库
建议 `hispeed-agent-skills`。将本文件夹放到仓库 `skills/hispeed-global-leads-research/`。为稳定规则创建受审核的 `stable` 分支。

## 2. 完成首次更新源配置
`config/update.json` 已预设 `liuxuan90/hispeed-agent-skills` 与 `stable` 分支。**发布后还需要创建 stable 分支**；在此之前自动更新会失败并回退至本地规则。
私有仓库需在**本地运行环境**安全设置环境变量 `HISPEED_SKILL_GITHUB_TOKEN`（最小权限的 contents:read token）。**不要将 token 写入 Skill 文件、Google Sheets 或 Agent 聊天。**

## 3. 安装
可在受 `skills.sh` CLI 支持的 Agent 环境下使用（仓库发布以后）：
```bash
npx skills add liuxuan90/hispeed-agent-skills --skill hispeed-global-leads-research -g
```
第一次安装可能需要指定 Agent；参考 `npx skills add --help`，确认对方 Agent 读取的是同一目录。`npx` 运行需满足工具当前 Node.js 版本要求。

## 4. 更新如何发生
每次 Agent 调用本 Skill 且平台允许本地执行 Python 时，按 `SKILL.md` 的启动指令运行：
```bash
python scripts/update_rules.py --quiet
```
该脚本从已配置的 GitHub `stable` 分支读取 manifest，验证 10 个允许更新的 Markdown 文件哈希，全部下载成功后才替换对应本地规则。失败会保留本地已可用规则，不中断研究。`rules_version` 记录在 `.rules-version.json`。
**不是所有平台都会自动执行 SKILL.md 中的脚本。** 要实现“运行 Skill 自动同步”，需要先用真实 Agent 测试 shell 权限、运行路径、会话缓存。没有脚本权限的云端 Agent 应采用平台自带同步或每次显式读取可信规则地址。

## 5. 首次测试话术
> 使用 hispeed-global-leads-research，目标国家：[填写]，客户类型：industrial laser marking distributors，目标数量：5 家。只做公开资料背调与英文开发信草稿，查询证据，输出四张表，并且不要发送邮件。历史客户名单目前不可用时须标记 REVIEW_REQUIRED。

## 6. 后续版本维护
只改 `references/*.md`：可每次运行前自动刷新；新增脚本、新工具权限、变更 `SKILL.md` 的安全边界：需人工审核、重新安装或通过受控安装器升级。保持受保护的 stable 分支；不要把任何潜客个人数据、API 凭证提交到仓库。

## 7. 当前还没接通的部分
Gemini/Google Sheets、Snov.io API、ChatGPT Work、企业微信机器人和 Muse 的权限与写入动作尚未在本包内配置，无法声称一键全自动。V1.0 重点先验证“找对公司、核实联系人、写出值得用的英文开发信”。
