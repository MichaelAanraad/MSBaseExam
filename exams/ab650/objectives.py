# Change these lines (plus DOMAINS and GROUPS) to build a practice exam for another certification.
EXAM = "AB-650"
EXAM_TITLE = "Administering Microsoft 365 and AI Services"
STUDY_GUIDE = "https://learn.microsoft.com/credentials/certifications/resources/study-guides/ab-650"

# Source: STUDY_GUIDE (fetched 2026-11-10)
# Allocation: D1 110 (22%), D2 207 (41%), D3 183 (37%) = 500,
# midpoints of the official weight ranges, normalized.
DOMAINS = {
    "1": ("Configure and manage Microsoft 365 tenants and workloads", "20-25%"),
    "2": ("Govern and secure Microsoft 365 tenants and workloads", "40-45%"),
    "3": ("Manage and secure AI services in Microsoft 365", "35-40%"),
}
# group id: (title, questions per objective, objectives)
GROUPS = {
    "1.1": ("Configure and manage a Microsoft 365 tenant", 8, [
        "Configure branding in a Microsoft 365 tenant, including logo, company URL, themes, and backgrounds",
        "Implement and manage domains",
        "Configure and manage organizational settings, including security and privacy settings and the organization profile",
        "Manage and monitor Microsoft 365 licenses, including group-based licensing and pay-as-you-go",
        "Manage and monitor licenses for AI services, including Microsoft 365 Copilot, Microsoft Agent 365, and Microsoft Copilot Studio",
        "Configure and use Microsoft 365 Backup, including setup, restore, and monitor",
        "Configure and review network connectivity insights",
        "Monitor the health of Microsoft 365 services by using Service health, including notification configuration"]),
    "1.2": ("Manage Microsoft 365 workloads", 9, [
        "Create and manage mailboxes, including shared mailboxes",
        "Create and manage teams in Microsoft Teams, including channels, owners, and members",
        "Configure settings for Copilot in Teams meetings, including transcription",
        "Create and manage SharePoint sites, including permissions",
        "Configure SharePoint and OneDrive for Copilot, including SharePoint Advanced Management, Microsoft Search in SharePoint, and site exclusions"]),
    "2.1": ("Manage identities in Microsoft Entra", 9, [
        "Create and manage Microsoft 365 users",
        "Manage guest users and external access settings",
        "Create and manage groups, including Microsoft 365 groups",
        "Manage roles for Microsoft 365, including Microsoft Entra Privileged Identity Management (PIM)",
        "Create and manage administrative units",
        "Create and manage contacts",
        "Perform bulk management, including Microsoft Graph PowerShell"]),
    "2.2": ("Implement and manage authentication and access in Microsoft Entra", 10, [
        "Configure and manage authentication methods",
        "Implement and manage Microsoft Entra Password Protection",
        "Configure self-service password reset (SSPR)",
        "Investigate and resolve authentication issues",
        "Implement and manage Microsoft Entra Conditional Access policies, including Microsoft Entra ID Protection and multifactor authentication"]),
    "2.3": ("Secure Microsoft 365 workloads", 10, [
        "Manage alerts in Microsoft Defender for Office 365",
        "Configure threat policies and rules in Defender for Office 365",
        "Investigate and respond to email and collaboration threats by using Defender for Office 365",
        "Configure and manage attack simulations, including training campaigns"]),
    "2.4": ("Protect data in Microsoft 365 by using Microsoft Purview", 10, [
        "Identify requirements for Microsoft Purview Data Loss Prevention (DLP) policies, including those for Exchange, SharePoint, OneDrive, Teams, endpoints, and Copilot",
        "Identify requirements for information protection, including sensitive information types, sensitivity labels, and sensitivity label policies",
        "Identify requirements for data lifecycle management, including retention labels, retention label policies, and retention policies",
        "Review and respond to DLP alerts for Microsoft 365 and AI services",
        "Monitor and secure AI activity by using Microsoft Purview Data Security Posture Management (DSPM)"]),
    "3.1": ("Enable and manage Microsoft 365 Copilot", 8, [
        "Assess tenant readiness for Copilot, including in-app experiences",
        "Identify and resolve data readiness issues for Copilot, including data leaks, data oversharing, and data compliance",
        "Manage web search for Copilot and Microsoft 365 Copilot Chat",
        "Configure Microsoft 365 Copilot Search",
        "Configure Copilot settings for a tenant, including self-service purchases, Copilot in admin centers, release preferences, AI disclaimer, and video and image generation",
        "Manage Copilot user experiences",
        "Manage Microsoft 365 Copilot Cowork",
        "Manage third-party AI providers",
        "Configure Copilot connectors"]),
    "3.2": ("Implement and manage agents in Microsoft 365 and Agent 365", 8, [
        "Manage the lifecycle workflows for agent identities by using Microsoft Entra Agent ID",
        "Secure agent access, including access packages and conditional access",
        "Manage agent owners",
        "Configure agent settings, including allowed agent types, sharing, templates, and user access",
        "Discover and manage Microsoft and third-party agents in the agent registry",
        "Review requests and publish or reject agents in the agent registry",
        "Install, block, or control access to agents in the agent registry, including uploading custom agents",
        "Manage tools in Agent 365"]),
    "3.3": ("Secure and govern agents by using Agent 365", 8, [
        "Monitor agent activity by using Agent 365",
        "Protect sensitive data by using Agent 365",
        "Evaluate compliance gaps by using Agent 365"]),
    "3.4": ("Monitor AI services in Microsoft 365", 6, [
        "Manage and monitor costs for AI services in Microsoft 365",
        "Monitor usage reports for Copilot in the Microsoft 365 admin center, including workload-level adoption details",
        "Monitor usage and adoption for AI services in Microsoft 365 by using the Copilot Control System",
        "Monitor service health by using the Copilot Control System"]),
}
TOTAL = 500  # question bank size; validate.py and build.py check against it
# Exceptions to the per-group count so the total is exactly TOTAL; narrow
# objectives get fewer questions, broad ones more.
OVERRIDE = {
    "1.1.1": 6, "1.1.5": 10, "1.1.6": 9,
    "2.1.4": 11, "2.1.6": 6, "2.1.7": 11, "2.2.5": 13,
    "3.1.7": 7,
}


def objectives():
    """{objective id: (text, target count)}"""
    out = {}
    for g, (_, n, objs) in GROUPS.items():
        for i, text in enumerate(objs, 1):
            oid = f"{g}.{i}"
            out[oid] = (text, OVERRIDE.get(oid, n))
    return out


if __name__ == "__main__":
    o = objectives()
    by_dom = {d: sum(n for k, (_, n) in o.items() if k[0] == d) for d in DOMAINS}
    print(len(o), "objectives,", sum(n for _, n in o.values()), "questions", by_dom)
    assert sum(n for _, n in o.values()) == TOTAL
    for g, (title, n, objs) in GROUPS.items():
        print(g, title, [o[f"{g}.{i}"][1] for i in range(1, len(objs) + 1)])
