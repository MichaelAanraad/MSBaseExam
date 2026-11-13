# Change these lines (plus DOMAINS and GROUPS) to build a practice exam for another certification.
EXAM = "GH-600"
EXAM_TITLE = "Developing in Agentic AI Systems"
STUDY_GUIDE = "https://learn.microsoft.com/credentials/certifications/resources/study-guides/gh-600"
# The study guide points to GitHub Docs for most topics, so refs may come from either site.
REF_PREFIXES = ("https://learn.microsoft.com/", "https://docs.github.com/")

# Source: STUDY_GUIDE (fetched 2026-11-12)
# Allocation: D1 88 (17.5%), D2 112 (22.5%), D3 62 (12.5%), D4 88 (17.5%),
# D5 88 (17.5%), D6 62 (12.5%) = 500, midpoints of the official weight ranges.
DOMAINS = {
    "1": ("Prepare agent architecture and SDLC processes", "15-20%"),
    "2": ("Implement tool use and environment interaction", "20-25%"),
    "3": ("Manage memory, state, and execution", "10-15%"),
    "4": ("Perform evaluation, error analysis, and tuning", "15-20%"),
    "5": ("Orchestrate multi-agent coordination", "15-20%"),
    "6": ("Implement guardrails and accountability", "10-15%"),
}
# group id: (title, questions per objective, objectives)
GROUPS = {
    "1.1": ("Integrate agents into the software development lifecycle (SDLC)", 9, [
        "Identify steps for agents to perform",
        "Identify and mitigate common anti-patterns in agents",
        "Define inputs, outputs, and success criteria for agents"]),
    "1.2": ("Define boundaries between planning, reasoning, and action", 9, [
        "Configure agent planning to be distinct from agent execution",
        "Configure an agent to output a structured plan",
        "Validate agent plans",
        "Prevent agent action until the agent checked and approved"]),
    "1.3": ("Configure observability and control for autonomous agents", 9, [
        "Plan and implement the degree of agent autonomy, including guardrails",
        "Configure agent to produce inspectable artifacts within standard development tooling",
        "Configure human intervention for autonomous agents without slowing delivery"]),
    "2.1": ("Select and configure agent tools", 6, [
        "Identify required tools",
        "Configure agent tools",
        "Configure agent tool permissions"]),
    "2.2": ("Configure MCP servers", 6, [
        "Add an MCP server as a tool to an agent",
        "Configure a GitHub remote MCP server",
        "Configure the MCP registries",
        "Configure MCP allow lists"]),
    "2.3": ("Integrate agents within development environments", 6, [
        "Evaluate the execution context for an agent",
        "Configure an agent's scope to a specific repository",
        "Configure an agent to be invoked in a CI workflow",
        "Configure an agent to use branch-based scope",
        "Enable an agent to perform autonomous actions, including creating branches and pull requests",
        "Configure an agent to handle environment-specific constraints"]),
    "2.4": ("Operate agents with safe execution paths and robust error handling", 6, [
        "Implement error handling",
        "Implement retries",
        "Implement rollbacks",
        "Implement escalation paths",
        "Implement traceability and accountability for agent actions"]),
    "3.1": ("Implement agent memory strategies", 7, [
        "Choose between short-term, long-term, and external memory",
        "Scope agent memory to task-relevant information",
        "Define memory expiration, pruning, and reset rules"]),
    "3.2": ("Persist agent state and manage context drift", 7, [
        "Capture task progress and decisions as durable artifacts",
        "Resume agent work without repeating steps or diverging from prior decisions",
        "Detect and correct drift during extended agent execution"]),
    "3.3": ("Ensure continuity of agent memory and state across tools and environments", 7, [
        "Share agent state",
        "Prevent conflicting context",
        "Prevent stale context"]),
    "4.1": ("Define success criteria and evaluation signals for agent tasks", 10, [
        "Specify expected outcomes and operational constraints for agent tasks",
        "Identify qualitative and quantitative evaluation signals to evaluate agents",
        "Align evaluation criteria with development intent",
        "Generate evaluation signals by using automated scanning tools"]),
    "4.2": ("Analyze agent failures and identify root causes", 10, [
        "Identify failures by using logs, plans, traces, outputs, and workflow artifacts",
        "Classify root causes, including reasoning errors, tool misuse, and context or environment issues"]),
    "4.3": ("Tune agent behavior based on evaluation results", 10, [
        "Revise instructions, workflows, or constraints",
        "Refine memory usage",
        "Refine tool usage and tool access"]),
    "5.1": ("Operate and manage multi-agent workflows", 7, [
        "Apply an orchestration pattern to coordinate multiple agents",
        "Configure agent isolation for parallel execution",
        "Detect and resolve agent conflicts, including overlapping code changes, duplicated effort, and contradictory outputs"]),
    "5.2": ("Configure observability for multi-agent behavior by using logs, artifacts, and operational signals", 7, [
        "Configure multi-agent workflows to produce artifacts suitable for review and audit",
        "Document key decisions, handoffs, and outcomes across agents",
        "Perform post-hoc analysis of multi-agent behavior"]),
    "5.3": ("Detect and respond to multi-agent failures and degraded behavior", 7, [
        "Identify failed, partial, or stalled agent executions",
        "Respond to degraded behavior or coordination across agents",
        "Implement multi-agent recovery patterns, including rollback and human-in-the-loop"]),
    "5.4": ("Manage the lifecycle of agents within multi-agent workflows", 7, [
        "Add agents to existing multi-agent workflows",
        "Update, reconfigure, or replace agents without disrupting active workflows",
        "Retire agents while preserving auditability and workflow continuity"]),
    "6.1": ("Define autonomy levels", 9, [
        "Classify agent actions by operational, security, and compliance risk to right-size human interventions",
        "Assign autonomy levels to maximize delivery speed while remaining compliant with organizational security and Responsible AI standards"]),
    "6.2": ("Implement guardrails and human-in-the-loop workflows", 9, [
        "Identify the subset of actions that require human judgment",
        "Block actions that violate defined security, compliance, or Responsible AI policies",
        "Scope permissions and execution contexts to enforce least-privilege access",
        "Require explicit authorization or controlled paths for irreversible or compliance-sensitive changes",
        "Preserve execution velocity by minimizing approvals that do not materially reduce risk"]),
}
TOTAL = 500  # question bank size; validate.py and build.py check against it
# Exceptions to the per-group count so the total is exactly TOTAL; narrow
# objectives get fewer questions, broad ones more.
OVERRIDE = {
    "1.2.2": 8, "1.2.3": 8,
    "2.1.3": 7, "2.2.2": 7, "2.2.4": 7, "2.3.5": 7,
    "3.3.1": 6,
    "4.1.3": 9, "4.3.2": 9,
    "5.1.1": 8, "5.1.2": 8, "5.1.3": 8, "5.3.3": 8,
    "6.1.1": 8,
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
