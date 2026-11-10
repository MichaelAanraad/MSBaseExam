# AB-650: audience and exam-specific rules

Audience (from the study guide): a Microsoft 365 and AI services administrator
who configures, manages, secures and governs Microsoft 365 tenants, workloads
and AI services, including Microsoft 365 Copilot, agents and connected AI
capabilities. Has experience with Microsoft 365 workloads and Microsoft Entra
ID, understands Defender XDR capabilities, and is familiar with Microsoft Graph
PowerShell. Works with architects and administrators for identity, security,
compliance, endpoints and applications.

- **Code language:** PowerShell only. Microsoft Graph PowerShell
  (`Connect-MgGraph`, `Get-MgUser`, `New-MgGroup`, `Set-MgUserLicense`,
  `Invoke-MgGraphRequest`, ...), Exchange Online PowerShell
  (`Connect-ExchangeOnline`, `New-Mailbox -Shared`, `Add-MailboxPermission`,
  ...), Security & Compliance PowerShell (`Connect-IPPSSession`), Microsoft
  Teams PowerShell and SharePoint Online Management Shell where Learn shows
  them. No Python, no C#. Never the retired MSOnline or AzureAD modules
  (`Connect-MsolService`, `Connect-AzureAD`); they may appear as distractors
  only when the rationale says they are retired.
- **Admin surfaces:** name the exact portal and path: Microsoft 365 admin
  center, Microsoft Entra admin center, Microsoft Defender portal, Microsoft
  Purview portal, Exchange admin center, Teams admin center, SharePoint admin
  center, Copilot Control System (Copilot page in the Microsoft 365 admin
  center), Agent 365. Portal-step ordering questions are realistic here.
- **Product names:** Microsoft Entra ID (not Azure AD), Microsoft Entra Agent
  ID, Microsoft Entra ID Protection, Microsoft Entra Privileged Identity
  Management (PIM), Microsoft Defender XDR, Microsoft Defender for Office 365,
  Microsoft Purview (not Microsoft 365 compliance center), Microsoft Purview
  Data Security Posture Management (DSPM) / DSPM for AI, Microsoft 365
  Copilot, Microsoft 365 Copilot Chat, Microsoft Copilot Studio, Microsoft
  Agent 365, SharePoint Advanced Management, Microsoft 365 Backup.
- **Least privilege:** in role questions the key is the narrowest built-in
  role that does the job (for example Exchange Administrator, Groups
  Administrator, User Administrator, License Administrator, AI Administrator,
  Security Operator). Broader roles (Global Administrator) and roles from the
  neighbouring admin center are the distractors. Verify every role name and
  what it can do on Learn.
- **Licensing:** state the license in the stem when a feature depends on it
  (Microsoft 365 E3 vs E5, Entra ID P1 vs P2, Defender for Office 365 Plan 1
  vs Plan 2, Microsoft 365 Copilot add-on). A license gap is a good buried
  constraint.
- **New features** (Agent 365, Copilot Cowork, Entra Agent ID, agent
  registry): test only what a Learn page you fetched describes. If Learn has
  little on a sub-topic, write fewer hard questions on it rather than
  inventing settings, and say so in your report.
