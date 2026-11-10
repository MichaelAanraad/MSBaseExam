# Open points from writers (for the verify pass)
## 1.2
- 1.2.2-07: Add-TeamChannelUser is public preview in Teams PowerShell.
- 1.2.2-09: shared channels with external users need B2B direct connect (inferred, shared-channels page not fetched).
- Distractor explanations: Teams Premium includes intelligent recap; Defender for Office 365 Plan 2 includes Threat Explorer (not fetched).
- 1.2.4-06: deleting a site from Deleted sites; based on New-SPOSite note.
- 1.2.5-06, 1.2.5-09: Restricted SharePoint Search retirement (new enablement blocked from July 31, 2026).
## 3.3 / 3.4
- RESOLVED 3.3.2-05: purview/ai-agent-365 lists agent-instance DLP only for Teams, OneDrive/SharePoint and email (agent instance or a security group in the policy); the Copilot location is not listed for agent instances. Key stands; distractor rationale only says it does not target agent-instance messages.
- RESOLVED 3.3.3-05: agent-details page says the Risks column and Security tab need a Microsoft E7 or Agent 365 license, so neither E5 Compliance nor Entra ID P2 can be a second answer. Key stands.
- RESOLVED 3.4.1: copilot-capacity-packs confirms 25,000 Copilot Credits per pack per month.
- NEW, not tested: audit operation for guardrails conflicts (audit-log-activities: Operation AIGuardrail; Management Activity API schema: RecordType AIGuardrail, Operation AIGuardrailApplied). 3.3.1-02 box 2 now asks for AIInferenceCall instead.
- NEW, not tested: AI regulation templates "count toward purchased premium licenses" (compliance-manager-assessments) vs "free for six months with Copilot or Agent licenses" (same page). 3.3.3-04 replaced (assessment status Incomplete -> Failed controls); 3.3.3-01 statement 2 replaced.
- NEW, not tested: Copilot Credits report alert threshold is 2,000 in one paragraph and 3,000 in another; 3.4.3-05 rationale no longer relies on it.
## 2.3
- 2.3.3-02: -RemoveAfter 45 explained as "remove after last used" for allow entries (inferred).
- 2.3.2-01: New-ATPProtectionPolicyRule as wrong step; parameters unverified.
## 3.2
- RESOLVED 3.2.4-05: Apply template rule (agent-settings) conflicts with the policy-template FAQ ("only new activation"). Question replaced: it now tests that the AI Administrator needs Attribute Assignment Administrator for custom security attribute policies (policy-template page). Access-package rights of AI Administrator also conflict (policy-template vs agent-actions) and are not tested.
- RESOLVED 3.2.3-01: not a second answer (groups are never owners, and owners are optional), but the distractor overlapped "An owner". Replaced with "A service principal as owner" (valid owner type, still optional, does not meet the sponsor requirement).
- Hidden vs shown-as-blocked external agents/plugins: pages still conflict; not tested, and the 3.2.7-02 rationale no longer relies on it.
## 2.1
- 2.1.2-07: $inv.InvitedUser.Id from New-MgInvitation (not seen in a sample).
- 2.1.5-04: activated directory role id as roleId for New-MgDirectoryAdministrativeUnitScopedRoleMember.
## 2.2
- 2.2.2-03: Password Protection scoring worked out by the writer (normalization, edit distance 1, five-point rule); recheck math.
- Legacy ID Protection risk policies retired Oct 1, 2026: check wording.
## 1.1
- 1.1.8-02: Get-MgServiceAnnouncementIssue -ServiceHealthIssueId (inferred from sibling cmdlet).
- 1.1.6-09: longer Backup recovery window increases storage cost (reasoned, not on Learn).
## 3.1
- RESOLVED 3.1.9-07: isRefinable is a real property attribute (Graph externalConnectors property resource).
- RESOLVED 3.1.1-06: Learn (assign-licenses-to-user-accounts-with-microsoft-365-powershell) states licenses can be assigned only when UsageLocation is set. Order rebuilt so exactly one sequence works.
- STILL NOT TESTED: Copilot Chat unpinning (pin-copilot-chat-navbar says it cannot be unpinned since Jan 2026; manage-copilot-chat still describes Do not pin) and Cowork Anthropic model scoping (cowork-access says tenant-wide; cowork-admin-governance says scopable). Rationales reworded so they do not depend on either.
- WATCH 3.1.5-04/3.1.5-08: "Copilot Release Preferences: General Availability" may be replaced by the unified release preferences experience (announced for November 2026).
