# Change these three lines (plus DOMAINS and GROUPS) to build a practice exam for another certification.
EXAM = "AI-500"
EXAM_TITLE = "Designing and Implementing Multi-Agent AI Solutions"
STUDY_GUIDE = "https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-500"

# Source: STUDY_GUIDE (fetched 2026-10-20)
# Allocation: D1 90 (18%), D2 170 (34%), D3 120 (24%), D4 120 (24%) = 500,
# midpoints of the official weight ranges, normalized.
DOMAINS = {
    "1": ("Architect multi-agent solutions", "15-20%"),
    "2": ("Develop multi-agent solutions in Azure", "30-35%"),
    "3": ("Evaluate, optimize, and monitor multi-agent solutions", "20-25%"),
    "4": ("Secure, govern, and deploy multi-agent solutions", "20-25%"),
}
# group id: (title, questions per objective, objectives)
GROUPS = {
    "1.1": ("Design logical architecture for multi-agent solutions", 6, [
        "Decompose goals and objectives into workflows, agents, and tools",
        "Design workflows, including agents, subagents, control loops, and human-in-the-loop",
        "Specify agent personas, scopes, boundaries, autonomy levels, and behavioral guidelines",
        "Specify tool scopes, permission boundaries, and authentication methods",
        "Specify appropriate protocols for communication, including between multiple agents and between agents and other components",
        "Design controls and functionality to support human-AI experience (HAX) and to adhere to responsible AI principles",
        "Design short-term and long-term memory architectures, including context sharing",
        "Match task demands to model family capacities"]),
    "1.2": ("Specify technology components to include in a multi-agent solution", 6, [
        "Specify integration components to coordinate agent-to-agent communication, agent-to-tool interactions, and agent-to-knowledge-source routing across a multi-agent production system",
        "Specify components for Zero Trust multi-agent solutions, including per-agent identity scoping, lateral movement prevention, and compliance control mapping for regulated deployments",
        "Specify multi-tier state persistence components that address session state, shared team state, and long-term semantic memory with lifecycle and tenant-isolation policies",
        "Specify compute components for multi-agent solutions that meet scalability, reliability, operational efficiency, security, and cost requirements",
        "Specify observability components, including cross-service trace correlation, structured logging of agent reasoning paths, and agent replay capture for reproducible debugging",
        "Specify monitoring components, including cross-agent coordination tracking, behavioral drift and quality regression detection, and automated remediation for agent failure patterns",
        "Specify developer tools and environment to support the Software Development Lifecycle (SDLC), including dev containers, Visual Studio Code extensions, command-line interface (CLI), dependency management, and AI instructions"]),
    "2.1": ("Design and implement advanced prompt engineering strategies in multi-agent solutions", 9, [
        "Design and implement advanced prompt engineering techniques, including examples, dynamic context injection, defensive guidelines, and prompt lifecycle management",
        "Design and implement context-aware multi-agent behaviors",
        "Design and implement a strategy for fine-tuning agents and models, including data and frequency"]),
    "2.2": ("Design and implement agent memory, context management, and knowledge integration", 9, [
        "Design and implement context management in single agents and between agents, including context accumulation, retrieval, injection, and compaction",
        "Design and implement single-agent and multi-agent memory strategies, including security, compliance, lifecycle, storage, and session management",
        "Design and implement a multi-agent RAG architecture, including chunking, embedding quality, and retrieval precision",
        "Design and implement knowledge integration for multi-agent consumption, including search, RAG, MCP-available sources, and semantic search"]),
    "2.3": ("Build and integrate tool ecosystems", 9, [
        "Integrate external resources, including function calling, specified tool use, and dynamic tool use",
        "Design and build MCP servers and clients, including Azure Functions, Azure Logic Apps, and Azure API Management",
        "Design tool error-handling and fallback mechanisms",
        "Implement tool result validation and quality checks"]),
    "2.4": ("Implement multi-agent orchestration", 9, [
        "Implement multi-agent orchestration patterns, including hub-and-spoke, sequential, parallel, peer-to-peer, and orchestrator-subagent",
        "Implement human-in-the-loop processes, including approval workflows, overrides, and edge case handling",
        "Design and implement a caching strategy, including prompt caching, semantic caching, and response caching",
        "Implement scaling and control of multi-agent spawning, batching, and concurrent execution",
        "Integrate existing agents into a multi-agent solution securely by using Agent2Agent (A2A) and/or MCP",
        "Implement multi-agent orchestration frameworks, including Agent Framework, LangChain, and LangGraph",
        "Implement advanced multi-agent capabilities by using Hugging Face Transformers",
        "Design middleware for reusable capabilities across the solution, including logging, authorization, and exception handling"]),
    "3.1": ("Design and implement evaluation and validation strategies for multi-agent solutions", 12, [
        "Design and implement a human review process to evaluate solutions in Foundry",
        "Design and implement evaluations for memory, knowledge, tools, and prompts"]),
    "3.2": ("Optimize prompt and model performance for multi-agent solutions", 12, [
        "Optimize task duration, including parallelism and rate limits",
        "Diagnose context window issues, including sliding-window amnesia, summary drift, vector-only recall, and entity continuity issues",
        "Design and implement continuous improvement, including LLM-as-a-judge frameworks, synthetic data generation, semantic optimization loops, and user feedback loops"]),
    "3.3": ("Design and implement observability and monitoring for multi-agent solutions", 12, [
        "Design a strategy for monitoring reliability, including agent health, workflow failures, trace correlation, drift detection, quality regression, and remediation",
        "Design a strategy for monitoring solution and platform availability, performance, reliability, and service-level agreement adherence",
        "Design and implement a strategy for optimizing token usage, including token limits, loop controls, and tool calls",
        "Design a strategy for monitoring and managing cost, including usage, quotas, allocations, and chargebacks",
        "Implement tracing in Foundry, including tokens, prompts, correlation IDs, alerting, and execution tracking"]),
    "4.1": ("Design and implement security for multi-agent solutions", 11, [
        "Specify and implement resource access, including identity-based access, network boundaries, access control policies, and role-based access control (RBAC)",
        "Design and implement authentication flows in a multi-agent solution, including user impersonation, on-behalf-of, API keys, and OAuth 2.0",
        "Design the secrets management and retrieval approach for multi-agent solutions by using Azure Key Vault, including secrets, certificates, key rotation, role-based access to secrets, and encryption",
        "Implement shift-left security principles, including the AI Red Teaming Agent in Foundry"]),
    "4.2": ("Design and implement guardrails for multi-agent solutions", 11, [
        "Design and implement a multi-intervention guardrail strategy covering user inputs, tool calls, tool responses, and outputs",
        "Design and implement custom guardrails for domain-specific constraints",
        "Design guardrail testing and validation, including using synthetic data"]),
    "4.3": ("Deploy multi-agent solutions to Azure", 11, [
        "Choose a release methodology, including Development-Test-Acceptance-Production (DTAP), blue/green, and canary",
        "Design and implement multi-environment release strategies, including rollback strategies, release management, and rollout",
        "Design and implement a strategy for testing, including unit tests, regression tests, integration tests, and automated evaluations",
        "Specify continuous integration and continuous deployment (CI/CD) requirements for integration and release, including infrastructure-as-code deployments and testing"]),
}
TOTAL = 500  # question bank size; validate.py and build.py check against it
# Exceptions to the per-group count so the total is exactly TOTAL.
OVERRIDE = {"2.4.8": 8, "4.3.4": 10}


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
