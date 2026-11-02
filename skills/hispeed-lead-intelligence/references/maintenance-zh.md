# 中文维护说明

本文件用于维护 Skill，不参与普通客户研究任务。

## 文件职责

- `SKILL.md`：执行入口和流程路由，保持精炼。
- `hispeed-company-facts.md`：Hispeed 稳定业务事实及对外表述边界。
- `evidence-policy.md`：事实、推断、未知和来源等级。
- `qualification-and-scoring.md`：ICP、同行分类、硬门槛和评分模型。
- `contact-email-policy.md`：联系人角色和邮箱证据等级。
- `first-email-policy.md`：第一封英文开发信规则。
- `workbook-schema.md`：在线表格逻辑结构、去重和安全写入。
- `feedback-and-versioning.md`：反馈标签和版本化优化。
- `assets/`：每次运行可复制填写的模板及 JSON Schema。

## 领导最终确认的两项规则

1. 国外激光设备同行不能自动视为竞争对手。必须同时判断直接竞争、采购、渠道、OEM/ODM 和系统集成机会；混合或证据不足时进入 `REVIEW`。
2. 第一封邮件正文采用 `Personalized Problem → Show You Solve It → CTA`。个性化问题必须来源于背调证据；推断使用探索式表达。

## 修改规则

- 核心护栏、证据语义和写入安全规则需要人工批准后修改。
- 评分权重或阈值变更时，更新模型版本，并记录样本量、变更理由和前后表现。
- Hispeed 产品、认证、保修或服务事实变化时，只修改 `hispeed-company-facts.md`，并重新核验官网来源。
- 表格平台变化时优先修改字段映射，不改变核心字段含义和企业身份键。
- 客户跟进、第三／第四封邮件、业务员分配和电话任务属于后续独立 Skill，不加入本 Skill。

## v1.1.0 维护记录

- Skill 版本：`1.1.0`。
- Company Record Schema：`v2`，新增独立 `known_customer` 门槛、资格边界带、完整度阻塞项、联系人时效和邮件时效字段。
- Scoring model：仍为 `v1`，权重和75分门槛未调整。
- 依据：一次21家候选的运行观察，样本不足30且未完成逐条人工复判，因此只修复定义和交付一致性，不声称完成评分校准。
- 旧v1记录不自动回写；需要迁移时另行人工批准。


