# 域名、DNS、SSL 与邮件保护

本参考仅涵盖域名绑定、DNS 记录、SSL 证书和邮件记录保护的单步教学规则；不提供应用排错、部署或业务代码实现。任何 Vercel 目标记录均以 **Dashboard 当前显示** 或当前官方诊断结果为准，绝不复用文档、截图或历史命令中的数值。

Last verified: 2026-08-03

官方依据：[设置自定义域名](https://vercel.com/docs/domains/set-up-custom-domain)、[域名排错](https://vercel.com/docs/domains/troubleshooting)、[使用 DNS](https://vercel.com/docs/domains/working-with-dns)、[使用 Nameservers](https://vercel.com/docs/domains/working-with-nameservers)、[vercel domains](https://vercel.com/docs/cli/domains)、[vercel dns](https://vercel.com/docs/cli/dns)。

## 不可跳过的变更前盘点

在添加、替换、删除或委派 DNS 前，先只读记录当前域名、注册商、权威 DNS 提供方、关联 Vercel 项目，以及现有 **A、CNAME、TXT、NS、MX、CAA** 记录的名称、值、优先级（如适用）和 TTL。记录应来自当前 DNS 控制台、DNS 区域导出或经遮盖的截图；看不到就标为“待确认”，不得猜测。

特别标识全部 **MX** 及其关联 TXT（例如邮件验证或发信策略）记录、业务子域、第三方验证记录和无关服务记录。它们不是域名指向网站所需的记录，也可能仍承载邮件或其他服务，**不得清空** DNS 区域，不得以“切换到 Vercel”为理由删除未逐项确认用途的记录。需要切换 Nameservers 时，先取得完整盘点并确认将保留的邮件与无关服务记录可以在目标 DNS 区重建；否则停止于只读确认。

## 状态地图：每轮只确认一个可观察状态

先在项目的 Domains 页面确认域名、项目、当前状态和 Dashboard 当前显示的要求。没有当前页面或官方诊断结果时，只要求一次只读检查，不提供固定记录值。

| 可观察状态 | 本轮只判断的事 | 后续路由 |
| --- | --- | --- |
| 尚未添加 | 目标域名、目标项目与现有承载服务是否已确认 | 先完成盘点，再在 Dashboard 添加域名 |
| 待验证 | Dashboard 是否要求 TXT 所有权验证，以及该 TXT 是否与现有邮件/验证 TXT 同名冲突 | 仅按当前页面显示的 TXT 新增或调整；等待验证状态更新 |
| Invalid Configuration | 当前 Dashboard 诊断要求的是记录、委派还是存在冲突 | 对照盘点后只处理一个明确冲突或缺失项；不要套用历史目标 |
| 证书等待（SSL pending） | 域名是否已正确指向 Vercel，以及 CAA、验证记录或通配符条件是否阻碍签发 | 保持当前诊断所需配置并等待；问题持续时转入官方诊断，不在此参考中排错 |
| Active | 当前项目、域名、SSL 状态和访问目标是否均为预期 | 只读确认；任何后续改动重新从盘点开始 |
| 转移中或由其他 Vercel 账户占用 | Dashboard 是否要求 TXT 验证，且是否只是允许本项目使用而非转移所有权 | 按当前 TXT 要求验证；所有权、团队和注册商转移另行确认，不作推断 |

“待验证”“Invalid Configuration”“证书等待”“Active”等文字以当前界面为准；界面措辞不同，只记录实际状态并按同一风险边界处理。

## Apex、子域与目标值

- **Apex 根域**（如 `example.com`）与**子域**（如 `www.example.com`）的 DNS 需求不同。仅在 Dashboard 当前显示或当前官方诊断结果明确要求时，才配置对应的 A 或 CNAME 记录；不得硬编码目标值。
- A、CNAME、TXT、NS、MX、CAA 可并存于同一 DNS 区，但记录名称、DNS 提供商规则和既有服务可能决定其是否冲突。修改前必须核对同名记录及其用途；不能仅凭记录类型判断可删除。
- 使用 Vercel Nameservers 是权威 DNS 委派变更，不是普通网站记录更新。**NS** 变更会影响整个域名的解析，应视为高风险；先完成邮件和无关服务迁移清单、回退方案与独立风险确认，再执行一个操作。
- 通配符域名（例如 `*.example.com`）需要 Vercel Nameservers 才能支持 Vercel 的通配符证书流程。通配符与 Nameservers 都是高风险：它们可能改变未知子域的解析或证书覆盖范围，未确认现有子域与邮件前不得继续。

## 邮件、SSL 与 CAA 保护

- **MX** 记录决定邮件投递路径。添加网站 A 或 CNAME 记录不等于可以删除 MX；切换 Nameservers 前必须把每条仍需保留的 MX 及关联 TXT 按盘点迁移到新 DNS 区，并在传播后只读核对。
- Vercel 会自动为已正确配置的域名申请 SSL 证书。若 SSL 仍在等待，不要反复切换记录，也不要宣称证书已经生效；先读取 Dashboard 诊断。
- **CAA** 会限制可签发证书的机构。若现有 CAA 存在，严格遵循 Dashboard 当前显示和 Vercel 官方 SSL 诊断的要求；不得因修复 SSL 而删除现有 CAA 或放宽其他服务所需限制。
- 对非通配符域名，Vercel 的证书验证依赖域名正确指向；对通配符域名，Vercel 要求 Nameservers 方法。遇到 `_acme-challenge` 或其他证书验证 TXT 时，先确认其归属和影响，再处理，不能将其视为无用记录。

## 计划切换、传播与回退

计划中的网站切换，应在变更窗口前根据当前 DNS 提供商能力和业务容忍度考虑降低待切换记录的 **TTL**；不得修改 MX、邮件验证或无关服务记录的 TTL 来替代网站切换准备。TTL 只是缓存策略，不保证即时切换。

每次 DNS 变更后必须等待 **传播** 并从 Dashboard 当前状态、权威 DNS 或官方诊断中确认结果；不要因本机缓存、单个地点或某一次访问就宣布全网完成。执行前记录旧记录、原权威 DNS、当前项目绑定和恢复路径。若新配置未达到预期，按已记录的回退方案恢复上一个已确认可用的记录或委派；回退也可能传播，不能承诺即时恢复。

## Dashboard 优先，CLI 只作当前能力补充

默认使用 Dashboard 的 Domains 页面添加域名、读取所需 DNS、查看验证与 SSL 状态；它是本任务的操作与证据来源。CLI 不是默认路线，也不得用旧命令输出替代 Dashboard 当前显示。

只有用户已明确需要命令行、CLI 已可用且当前官方文档支持该能力时，才在不暴露凭据的前提下使用官方命令读取当前信息或验证。例如，先由当前官方文档确认 `vercel domains inspect` 或 `vercel domains verify` 是否适用于该账号、团队和项目，再以其输出中的当前诊断为准。若命令与 Dashboard 结果不一致，停止修改，保留两份证据并要求人工确认；不得自行选择其一。
