# GH-600: audience and exam-specific rules

Audience (from the study guide): a developer who operates, integrates,
supervises and governs AI agents inside production SDLC workflows, with GitHub
as the system of record and control plane. Operates agent workflows, supervises
autonomous behavior with GitHub controls, evaluates and tunes agent output with
scans and artifacts, configures custom agents, and coordinates multi-agent
execution safely. Has experience with the SDLC, GitHub workflows and controls,
code quality, security and review practices, and coding agents including GitHub
Copilot, MCP servers, custom instructions, custom agents, tools, and Copilot
setup steps. Works with architects, platform and DevOps engineers, developers,
product managers and security engineers.

- **Sources:** the study guide links to GitHub Docs (docs.github.com) for every
  domain, plus the Learn modules *Foundations of Agentic AI in GitHub*,
  *Designing Agent Architecture and SDLC Integration* and *Tooling, MCP, and
  Agent Execution Environments*. Search Microsoft Learn first; for GitHub
  product behavior, fetch the GitHub Docs page and use it as `ref`
  (`REF_PREFIXES` in `objectives.py` allows both sites). Never invent a URL.
- **Code and config language:** YAML and Markdown files as GitHub uses them:
  custom agent profiles (`.github/agents/*.agent.md` with YAML frontmatter:
  `name`, `description`, `tools`, `model`, `mcp-servers`,
  `disable-model-invocation`, `user-invocable`), custom instructions
  (`.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`
  with `applyTo`, `AGENTS.md`), the `copilot-setup-steps.yml` workflow (job
  name `copilot-setup-steps`), GitHub Actions workflow YAML, MCP server JSON
  (`mcpServers`, `type`, `command`, `url`, `tools`), and `gh` or Copilot CLI
  commands where GitHub Docs shows them. No Python or C# unless a GitHub Docs
  page for the Copilot SDK shows it.
- **Product names:** GitHub Copilot, Copilot cloud agent (the current name for
  Copilot coding agent; use the older name only if the fetched page does),
  Copilot code review, Copilot CLI, Copilot Memory, custom agents, custom
  instructions, Copilot setup steps, GitHub MCP Server (remote and local), MCP
  registry, GitHub Actions, rulesets, branch protection, CodeQL, secret
  scanning, Dependabot, GitHub Advisory Database, GitHub Advanced Security,
  audit log, Microsoft Entra ID (not Azure AD).
- **Guardrail facts worth testing** (verify each on the fetched page): Copilot
  cloud agent pushes only to its own `copilot/` branch or the pull request
  branch, opens draft pull requests, cannot approve or merge, workflows wait for
  **Approve and run workflows** by default, the requester cannot approve the
  pull request, the firewall limits internet access, commits are co-authored
  and signed and link to the session log.
- **Distractors:** same family. For example four `tools` values, four places
  to store guidance (custom instructions, Copilot Memory repository fact,
  Copilot Memory user preference, custom agent profile), four built-in
  validation tools (CodeQL, secret scanning, Advisory Database check, Copilot
  code review), or four GitHub controls (ruleset, branch protection, required
  check, environment protection rule).
- **Concepts without one product answer** (anti-patterns, orchestration
  patterns, drift, autonomy levels, retries and rollbacks): frame them in a
  GitHub scenario (issues, pull requests, Actions, rulesets, session logs) and
  ground them on the Learn modules or GitHub Docs. Preview features: test only
  what a fetched page describes.
