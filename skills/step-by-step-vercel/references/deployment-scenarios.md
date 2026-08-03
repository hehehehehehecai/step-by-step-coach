# 部署场景

本参考仅涵盖项目导入、构建配置、Preview、Production、Functions、重新部署、Promote 与 Rollback 的详细单步教学规则；不提供 DNS、业务代码实现或排错流程。

Last verified: 2026-08-03

官方依据：[Deploying Git Repositories with Vercel](https://vercel.com/docs/git)、[Configuring a Build](https://vercel.com/docs/builds/configure-a-build)、[Deploying to Vercel](https://vercel.com/docs/deployments)、[Promoting Deployments](https://vercel.com/docs/deployments/promoting-a-deployment)、[Instant Rollback](https://vercel.com/docs/instant-rollback)、[Vercel Hobby Plan](https://vercel.com/docs/plans/hobby)。

## 状态地图：先确认一个状态，再选择一轮动作

不要把下列内容作为一次性清单交给用户。每轮先确认项目、目标环境、最后完成的动作和 Dashboard 中可见的单一状态；信息不足时，只要求一个只读检查或一个澄清回答。

| 可观察状态 | 本轮只判断的事 | 后续路由 |
| --- | --- | --- |
| 未导入 | 是否已有可访问的 Git 仓库，以及 Git 提供方 | 转入“导入” |
| 已导入、未部署 | Framework Preset 与构建配置是否已核对 | 转入“配置”或 Preview |
| Building | 当前构建仍在运行 | 等待可观察状态，不并行改配置 |
| Failed | Deployment 显示失败 | 停止本参考；转入排错场景，只索取经遮盖的错误摘要或日志位置 |
| Ready | 部署已成功生成 URL | 按其环境转入 Preview 验证或 Production 状态确认 |
| Preview | 非生产部署可访问 | 默认先完成与目标有关的 Preview 验证 |
| Production | 生产部署存在 | 仅确认是否为 Current；生产变更必须先走高风险门禁 |
| Promoted | 部署已被提升，但不必然是当前承载生产域名的部署 | 只读确认该部署是否已成为 Current；未成为 Current 时，不把它当作线上版本 |
| Current | 当前由生产域名指向、正在服务用户的部署 | 确认目标 URL 与 Production 环境；不可据此推断外部资源正常 |
| Rolled back | 生产域名已回指旧部署 | 确认自动分配状态和目标 URL；不要假定环境变量或外部数据已回退 |

## 导入：GitHub 主路线与通用回退

1. **GitHub 主路线**：若仓库位于 GitHub 且用户拥有相应访问权，只指导其在 Dashboard 新建项目并选择仓库；一次只做导入页面上的一个选择，随后等待导入结果。Vercel 为 GitHub 仓库提供每次分支推送的 Preview，并将生产分支的更新部署为 Production。
2. **GitLab / Bitbucket 通用回退**：若仓库位于 GitLab 或 Bitbucket，仍先在 Dashboard 的新建项目流程中选择相应 Git 提供方和仓库；不可因界面或权限差异猜测按钮、授权状态或部署已创建。若用户的提供方、权限或仓库未出现在列表中，停止导入教学，只要求一个只读的可见错误或权限状态。
3. 项目已导入但尚未形成部署时，先转入配置确认；不要重复导入，也不要把导入成功当作构建成功。

## 配置：只核对，不把不确定默认值当事实

Vercel 会自动检测很多框架并设置默认值，但每个项目在首次部署或变更前只核对当前页面显示的一个配置项。依次可能需要确认的项目是：**Framework Preset**、**Root Directory**、Build Command、Output Directory、Install Command 与运行时版本（例如 Node.js Version）。

- **Framework Preset**：先记录检测结果；无法确认时不要手工改为其他框架。
- **Root Directory**：确认应用在仓库中的实际目录。此设置会限制构建可访问的目录，并影响安装路径；变更仅从下一次部署生效。改变 Root Directory 是高风险动作，必须先走高风险门禁。
- **Build Command / Output Directory / Install Command**：优先核对自动检测值或当前覆盖值。Output Directory 指向构建后静态托管的目录；Install Command 由 Vercel 自动检测时，不要无证据覆盖。
- **运行时版本**：仅确认当前项目设置或受支持运行时；不要在本参考中指导修改业务代码或运行时实现。

配置改动尚未产生新部署时，状态仍是“已导入、未部署”；不得声称改动已经生效。

## Preview 优先与 Production 门禁

正常情况下，构建成功后先在 **Preview** 验证目标 URL、部署环境和用户当前目标；只有用户能独立确认例外理由时，才讨论跳过 Preview 的请求。即使用户要求跳过、时间紧急或声明自行承担后果，也不得绕过高风险确认。

以下动作必须单独占用一轮高风险确认，并完全遵守核心 Skill 的“四标题风险确认卡”契约：首次或再次发布到 **Production**、将部署 **Promote** 到 Production、**Rollback**、删除项目、改变 **Root Directory**，以及可能影响线上服务的 Production 重新部署。确认卡只能说明“准备做什么”“影响对象”“可能不可逆后果”“更安全的替代方案”并索取“明确确认”；不得在该轮提供点击路径、命令或可执行生产操作。

更安全的替代方案默认是先完成 Preview 验证；对删除项目，替代方案是先保留项目并只读确认不再使用；对 Root Directory 变更，替代方案是先在 Preview 用已确认的目录验证。

## Production、Promote、重新部署与 Rollback

- **Production**：生产分支的新提交通常会触发 Production 部署。获得明确确认后，仍只给一个 Dashboard 操作；完成后必须由用户提供 URL 可访问、环境为 Production 且部署状态正确的证据。
- **Promote**：Preview 可以提升到 Production；Vercel 对“已提升/当前”的状态有区别，生产域名当前指向的部署是 **Current**。Promote 是高风险，确认前不能给操作路径。
- **重新部署**：仅在用户已确认目标部署和原因后处理。重新部署会重新运行该部署的构建；若目标为 Production 或可能影响线上服务，按高风险处理。不要把重新部署说成回滚。
- **Rollback**：即时回滚会把生产域名指向曾服务 Production 的部署，不会重新构建；旧部署的构建配置、环境变量和外部 API、数据库或 CMS 的状态可能与当前状态不一致。Rollback 是高风险，先完成独立确认，再只给一个 Dashboard 操作。回滚后，自动分配 Production 域名会关闭；不要假定后续生产分支推送会自动上线。

## Hobby 套餐：先确认，再给免费替代

不得假定用户的套餐或页面能力。若当前为 **Hobby**，Vercel 官方文档说明即时 Rollback 只能回到紧邻的上一部署；Pro 和 Enterprise 才可从符合资格的历史 Production 部署中选择。若所需历史版本不符合 Hobby 的可回滚范围，更安全且无需升级的替代是：先将已知良好版本创建为 Preview 并验证，再由用户在独立高风险确认后决定是否发布为新的 Production 部署。不要承诺免费套餐能够恢复任意历史部署。

Hobby 还有使用与协作限制（例如部署次数、构建资源及私有组织仓库的 Git 部署限制）。遇到页面提示套餐限制时，只记录实际提示和当前套餐；不得猜测配额余量或暗示升级必然解决。可用的免费替代优先是减少无关重新部署、先用 Preview 验证，或等待限制窗口恢复；是否升级由用户自行决定。

## Functions 与外部资源：只验证连接结果

本参考不指导 Functions、数据库、第三方 API 或其他业务代码的实现。若用户已部署含 **Functions** 的项目，只在部署为 Ready 后选择一个不含密钥的验证目标：确认函数部署状态与公开/受保护 URL 的预期响应，或确认 Vercel 页面中可见的运行时状态。外部资源连接只能基于该单次可观察结果判断“当前请求是否得到预期响应”；不能据此推断凭据安全、数据正确、写入成功或所有依赖健康。

验证证据不得包含密钥、Token、Cookie、连接串、完整环境变量值或未遮盖的敏感日志。出现构建或运行错误时，停止本参考并转入排错场景；不要在这里修改业务代码。
