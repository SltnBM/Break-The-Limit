<p align="center">
  <img src="assets/banner.png" alt="Break-The-Limit" width="100%"/>
</p>

<h1 align="center">Break-The-Limit</h1>

<p align="center">
  Terminal-native AI offensive security &amp; bug bounty toolkit — powered by <code>breach</code>.
</p>

<p align="center">
  Authorized security testing only — see <a href="#disclaimer">Disclaimer</a>.
</p>

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <a href="https://github.com/SltnBM/Break-The-Limit/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/SltnBM/Break-The-Limit/tests.yml?branch=main&style=flat-square&label=tests" alt="Tests"></a>
</p>

---

## Overview

Break-The-Limit (`breach`) is a terminal-native AI offensive security and bug bounty toolkit featuring native tactical playbook injection (`breach skills`), a multi-provider LLM router (including `9Router`, free/community OpenAI-compatible endpoints, local Ollama, and Google OAuth), and built-in **Untrusted Output Delimiter** protection against indirect prompt injection from target responses.

| Component | Purpose | Path |
|---|---|---|
| `breach` CLI | Primary dispatcher for setup, interactive chat, recon, active hunting, validation, and reporting | [`bughunter/engine.py`](bughunter/engine.py) |
| Native Skill Engine | Loader that injects 25 tactical offensive playbooks directly into live AI sessions | [`bughunter/tools/skill_loader.py`](bughunter/tools/skill_loader.py) |
| Interactive Agentic Shell | Free-form `breach chat` shell with HTTP probing, CVE lookup, local shell execution, and prompt-injection delimiters | [`bughunter/tools/chat_agent.py`](bughunter/tools/chat_agent.py) |
| Multi-Provider Brain | Unified LLM client supporting Google OAuth, `9Router`, custom/free endpoints, local models, and cloud APIs | [`bughunter/brain.py`](bughunter/brain.py) |
| 25 Tactical Skills | Offensive playbooks across Web, API, Business Logic, 0-Day Killchain, Cloud, Mobile, AI/MCP, and Web3 | [`skills/`](skills/) |
| 42 Slash Commands | Structured workflow templates for external agent harnesses | [`commands/`](commands/) |
| MCP Bridges | Local MCP server plus Burp Suite, Caido, and HackerOne integrations | [`bughunter/mcp/`](bughunter/mcp/) |

---

## Quick Start

Get `breach` running in under 60 seconds:

```bash
git clone https://github.com/SltnBM/Break-The-Limit.git && cd Break-The-Limit
./install.sh --agent standalone
breach setup && breach chat
```

---

## Installation Guide

Choose the installation method that matches your environment and workflow.

### 1. Prerequisites

| Requirement | Minimum Version | Purpose |
|---|---|---|
| Python | `3.10+` | Core `breach` engine, skill loader, and interactive agent |
| Git | `2.x+` | Cloning and updating the repository |
| `pip` / `venv` | Standard Python packaging | Installing dependencies (`requests`, `pytest`, optional `ollama` / `mcp`) |
| External Recon Tools *(optional)* | Checked via `breach arsenal` | `subfinder`, `httpx`, `nuclei`, `ffuf`, `katana`, `dalfox`, `sqlmap`, etc. |

### 2. Option A — System-Wide Standalone CLI (Recommended)

Installs `breach` globally into `/usr/local/bin/breach` (or `~/.local/bin/breach`) and installs Python dependencies automatically so you can run `breach` from any directory without activating a virtual environment.

```bash
# 1. Clone the repository
git clone https://github.com/SltnBM/Break-The-Limit.git
cd Break-The-Limit

# 2. Run the standalone installer
chmod +x install.sh
./install.sh --agent standalone

# 3. If ~/.local/bin is not in your PATH, add it:
export PATH="$HOME/.local/bin:$PATH"

# 4. Verify the installation
breach --help
breach skills
```

### 3. Option B — Python Virtual Environment (Isolated / Development)

Use this method on Linux distributions with PEP 668 (`externally-managed-environment`, such as Kali Linux, Ubuntu 24.04+, or Arch) or when developing and running the test suite.

```bash
# 1. Clone the repository
git clone https://github.com/SltnBM/Break-The-Limit.git
cd Break-The-Limit

# 2. Create and activate an isolated virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install Break-The-Limit in editable mode with test dependencies
pip install --upgrade pip
pip install -e ".[test]"

# 4. Verify CLI entrypoints and test suite
breach --help
breach-agent --help
pytest -q
```

> **Tip:** To install the editable `breach` entrypoint straight into `~/.local/bin` without activating a virtualenv every time on PEP 668 systems:
> ```bash
> pip install --user --break-system-packages -e .
> ```

### 4. Option C — AI Coding Harness Plugin Install

In addition to the standalone `breach` CLI, you can install the 25 tactical skills, 42 slash commands, rules, and specialized agents directly into external AI coding harnesses:

| Target Harness | Global Install Command | Project-Local Install Command | Destination (Global) |
|---|---|---|---|
| Antigravity / Gemini | `./install.sh --agent antigravity` | `./install.sh --agent antigravity --project` | `~/.gemini/config/` |
| Claude Code | `./install.sh --agent claude` | `./install.sh --agent claude --project` | `~/.claude/` |
| OpenCode | `./install.sh --agent opencode` | `./install.sh --agent opencode --project` | `~/.config/opencode/` |
| Codex | `./install.sh --agent codex` | `./install.sh --agent codex --project` | `~/.codex/` |
| Pi Agent | `./install.sh --agent pi` | `./install.sh --agent pi --project` | `~/.pi/agent/` |
| Shared `.agents` | `./install.sh --agent agents` | `./install.sh --agent agents --project` | `~/.agents/skills/` |
| MCP Server Setup | `./install.sh --agent mcp` | — | Prints MCP config & installs `mcp>=2.2.0` |
| All Supported Targets | `./install.sh --agent all` | — | Installs across all harnesses above |

### 5. Post-Install: Provider Setup & External Arsenal Check

After installing `breach`, configure your AI provider and inspect your external offensive tool binaries:

```bash
# Configure AI provider (9Router, Custom Free Provider, Google OAuth, Ollama, Groq, etc.)
breach setup

# Check installed external recon & exploitation tools (nuclei, subfinder, httpx, ffuf, etc.)
breach arsenal
```

### 6. Updating & Uninstalling

```bash
# Update an existing clone
cd Break-The-Limit
git pull origin main
./install.sh --agent standalone

# Uninstall standalone CLI (preserves ~/.bughunter/config.json)
./uninstall.sh --agent standalone

# Uninstall everything and purge saved provider configuration
./uninstall.sh --agent all --purge-config --yes
```

---

## Usage

### Core CLI Commands

Use the `breach` CLI to configure providers, inspect or inject tactical skills, and execute recon or hunting workflows.

| Task | Command |
|---|---|
| Configure AI provider (interactive wizard, including `9Router` & Custom URLs) | `breach setup` |
| Quick setup for a local `9Router` instance (`http://localhost:20128/v1`) | `breach setup --provider 9router` |
| List available models on the active provider | `breach models` |
| List all 25 tactical offensive skills | `breach skills` |
| Recommend skills based on target signals (e.g., `graphql`, `jwt`, `nextjs`) | `breach skills recommend graphql` |
| Launch the interactive offensive security chat agent | `breach chat` |
| Launch chat pre-loaded with specific tactical playbooks | `breach chat --skill js-deep-miner,zero-day-killchain` |
| Run the automated recon and vulnerability hunting pipeline | `breach hunt example.com` |
| Validate a finding through the 7-Question Gate | `breach validate "IDOR on /api/v2/orders/{id}"` |
| Generate a platform-ready bug bounty report | `breach report` |

### In-Chat Slash Commands (`breach chat`)

Inside `breach chat`, the AI operates in a direct, zero-lecture offensive mode by default (without rigid phase locking) and responds to live slash commands.

| In-Chat Command | Description |
|---|---|
| `/skill <name>` | Inject a tactical playbook (e.g., `/skill zero-day-killchain`) into the active session |
| `/skill clear` | Unload all injected skills from the current session context |
| `/skills` | Show currently loaded skills and list all 25 available playbooks |
| `/target <domain>` | Load `recon/<target>` and `findings/<target>` artifacts into the active session |
| `/phase <0-5\|off>` | Lock focus to a specific hunting phase (`0`–`5`), or set `off` for unrestricted tactical mode |
| `/auto` | Toggle automatic approval for tool executions (`http_fetch`, `run_command`, `web_search`, `read_file`) |
| `/clear` | Clear the current conversation history |

---

## Security Architecture & Operator Control

Break-The-Limit is engineered to keep full control in the hands of the human operator while defending the AI agent against malicious target responses:

- **Direct Tactical Mode:** `breach chat` treats the user as an authorized operator—no scope paperwork prompts, no compliance lectures, and no mandatory phase gates unless explicitly enabled via `--phase` or `/phase`.
- **Untrusted Output Delimiter (`prompt_safety.py`):** Every HTTP response (`http_fetch`), shell output (`run_command`), web search result (`web_search`), file read (`read_file`), and recon summary is wrapped in randomized `<untrusted_target_output_XXXXXXXX>` boundaries with role-takeover neutralizing filters so target servers cannot hijack the AI agent via indirect prompt injection.
- **Interactive Tool Approval (`[Y/n/a]`):** Every active command or HTTP request displays the exact command/URL and waits for operator confirmation before execution (or runs hands-free when `--auto` / `/auto` is enabled).

---

## Supported AI Providers

Configure any provider via `breach setup`. Full default model mappings are documented in [Supported AI Models](docs/supported-models.md).

### Custom, Community & Free Routers

| Provider | Auth | Notes |
|---|---|---|
| `9router` | Custom URL | Built-in preset for `http://localhost:20128/v1` with automatic `/v1/models` discovery |
| `custom` | Custom URL | Supports any free/community OpenAI-compatible provider, `LM Studio`, `vLLM`, `llama.cpp`, or self-hosted gateway |

### Subscription / OAuth & Local

| Provider | Auth | Notes |
|---|---|---|
| `antigravity` (`agy`) | OAuth | Access Gemini AI Pro & Claude models via Google OAuth (no API key required) |
| `gemini-oauth` | OAuth | Google OAuth CLI credentials (`~/.bughunter/google_oauth.json`) |
| `ollama` | Local | 100% free and offline via local `OLLAMA_HOST` daemon |

### Cloud API & Multi-Model Gateways

| Provider | Auth | Notes |
|---|---|---|
| `groq` | API key | `GROQ_API_KEY`, ultra-fast inference with free tier |
| `cerebras` | API key | `CEREBRAS_API_KEY`, low-latency inference |
| `deepseek` | API key | `DEEPSEEK_API_KEY`, DeepSeek V4 models |
| `gemini` | API key | `GEMINI_API_KEY`, Google Gemini API |
| `claude` | API key | `ANTHROPIC_API_KEY`, Anthropic Claude API |
| `openai` | API key | `OPENAI_API_KEY`, OpenAI API |
| `grok` | API key | `XAI_API_KEY`, xAI Grok API |
| `kimi` | API key | `MOONSHOT_API_KEY`, Moonshot AI API |
| `mistral` | API key | `MISTRAL_API_KEY`, Mistral AI API |
| `together` | API key | `TOGETHER_API_KEY`, open-weight cloud models |
| `perplexity` | API key | `PERPLEXITY_API_KEY`, search-grounded models |
| `openrouter` | API key | `OPENROUTER_API_KEY`, multi-model gateway |
| `orcarouter` | API key | `ORCAROUTER_API_KEY`, multi-model gateway |
| `fluxion` | API key | `FLUXION_API_KEY`, multi-model gateway |
| `requesty` | API key | `REQUESTY_API_KEY`, multi-model gateway |
| `litellm` | API key | `LITELLM_API_KEY`, unified proxy for 100+ providers |

---

## Tactical Skills & Slash Commands

### Tactical Skills (25)

All 25 playbooks in [`skills/`](skills/) can be browsed with `breach skills` and injected directly into `breach chat` via `--skill <name>` or `/skill <name>`.

| Domain | Count | Playbooks (`skills/`) |
|---|---|---|
| Core & Chaining | 3 | `btl-methodology`, `btl-master-hunt`, `exploit-chaining` |
| Web, API & 0-Day | 5 | `web-exploit-matrix`, `business-logic-assault`, `zero-day-killchain`, `graphql-offensive`, `payload-arsenal` |
| Code & JS Analysis | 3 | `js-deep-miner`, `client-js-reverse`, `taint-trace-audit` |
| Recon, Auth & PII | 3 | `surface-recon`, `pii-exposure-hunter`, `cred-spray-ops` |
| Cloud, CI/CD & Mobile | 3 | `cloud-post-exploit`, `pipeline-exploitation`, `mobile-runtime-audit` |
| AI, Agentic & MCP | 3 | `ai-prompt-redteam`, `agentic-system-audit`, `mcp-security-audit` |
| Web3 & Token Audit | 2 | `defi-contract-audit`, `token-rugpull-audit` |
| Triage & Reporting | 3 | `impact-gate`, `bounty-reporting`, `vrt-triage-reporting` |

### Slash Commands (42)

Twelve core commands are highlighted below; expand the dropdown for the complete 42-command catalog in [`commands/`](commands/).

| Category | Command | Purpose |
|---|---|---|
| Recon | `/recon` | Run the full reconnaissance pipeline |
| Recon | `/scope` | Verify target assets against program scope rules |
| Recon | `/surface` | Rank and prioritize the discovered attack surface |
| Hunt | `/hunt` | Launch active vulnerability testing |
| Hunt | `/autopilot` | Run the autonomous end-to-end hunting loop |
| Hunt | `/chain` | Combine multiple primitives into a high-impact exploit chain |
| Validate & Report | `/validate` | Run the 7-Question Gate on a candidate finding |
| Validate & Report | `/triage` | Perform rapid reportability and severity triage |
| Validate & Report | `/report` | Generate a submission-ready vulnerability report |
| Utilities | `/pickup` | Resume a previous target hunting session |
| Web3 & OSINT | `/web3-audit` | Audit Solidity/Rust smart contracts |
| Web3 & OSINT | `/token-scan` | Scan tokens and meme coins for rug pull mechanics |

<details>
<summary>Full list of 42 Slash Commands (<code>commands/</code>)</summary>

| Category | Command | Purpose |
|---|---|---|
| Recon | `/recon` | Run the full reconnaissance pipeline |
| Recon | `/scope` | Verify target assets against program scope rules |
| Recon | `/scope-aggregate` | Aggregate in-scope assets across bug bounty platforms |
| Recon | `/surface` | Rank and prioritize the discovered attack surface |
| Recon | `/cloud-recon` | Discover public cloud buckets and origin IPs |
| Recon | `/param-discover` | Mine hidden HTTP parameters on endpoints |
| Recon | `/secrets-hunt` | Scan JS bundles and repositories for leaked credentials |
| Recon | `/takeover` | Detect dangling DNS records and subdomain takeover candidates |
| Recon | `/portscan` | Scan target hosts for exposed network services |
| Recon | `/intel` | Fetch CVE intelligence and disclosed bounty reports |
| Hunt | `/hunt` | Launch active vulnerability testing |
| Hunt | `/autopilot` | Run the autonomous end-to-end hunting loop |
| Hunt | `/chain` | Combine multiple primitives into a high-impact exploit chain |
| Hunt | `/bypass-403` | Test header, path, and verb mutations against HTTP 403/401 |
| Hunt | `/cors` | Test endpoints for exploitable CORS misconfigurations |
| Hunt | `/crlf` | Probe for CRLF and host header injection |
| Hunt | `/domxss` | Confirm DOM XSS sinks and sources in headless browser context |
| Hunt | `/jwt-scan` | Analyze and test JWT tokens for cryptographic flaws |
| Hunt | `/nosqli` | Probe endpoints for NoSQL operator and syntax injection |
| Hunt | `/oob` | Correlate out-of-band callbacks via Interactsh |
| Hunt | `/scan-cves` | Execute targeted Nuclei CVE sweeps |
| Hunt | `/sast` | Run static analysis rules against source repositories |
| Hunt | `/llm-app-audit` | Perform black-box security audits on AI/agent applications |
| Hunt | `/llm-redteam` | Execute prompt injection and guardrail bypass tests |
| Hunt | `/spray` | Run lockout-aware credential spraying with safety guards |
| Validate & Report | `/validate` | Run the 7-Question Gate on a candidate finding |
| Validate & Report | `/triage` | Perform rapid reportability and severity triage |
| Validate & Report | `/verify` | Independently re-verify a PoC bundle |
| Validate & Report | `/report` | Generate a submission-ready vulnerability report |
| Validate & Report | `/poc` | Scaffold a reproducible Proof-of-Concept bundle |
| Validate & Report | `/screenshot` | Capture visual evidence across live hosts |
| Validate & Report | `/remember` | Record confirmed findings into persistent hunt memory |
| Utilities | `/arsenal` | Check installed external security tools and install hints |
| Utilities | `/dashboard` | Launch the local hunt telemetry and findings dashboard |
| Utilities | `/memory-gc` | Rotate and compact hunt-memory JSONL logs |
| Utilities | `/oracle` | Rank leads using historical pattern memory |
| Utilities | `/pickup` | Resume a previous target hunting session |
| Web3 & OSINT | `/web3-audit` | Audit Solidity/Rust smart contracts |
| Web3 & OSINT | `/token-scan` | Scan tokens and meme coins for rug pull mechanics |
| Web3 & OSINT | `/wordlist-gen` | Generate target-specific password and path wordlists |
| Web3 & OSINT | `/osint-employees` | Gather employee and email format OSINT |
| Web3 & OSINT | `/breach-check` | Rank wordlists via k-anonymity breach frequency |

</details>

---

## MCP Integrations

Break-The-Limit includes Model Context Protocol (MCP) servers and clients to bridge `breach` with HTTP intercepting proxies and bug bounty platforms.

| Integration | Purpose | Path |
|---|---|---|
| Break-The-Limit MCP | Local MCP server (`breach mcp serve`) with automatic secret redaction | [`bughunter/mcp/bughunter-mcp/`](bughunter/mcp/bughunter-mcp/) |
| Burp Suite MCP Client | Bridge client for Burp Suite proxy history and Repeater | [`bughunter/mcp/burp-mcp-client/`](bughunter/mcp/burp-mcp-client/) |
| Caido MCP Client | Bridge client for Caido proxy traffic and replay | [`bughunter/mcp/caido-mcp-client/`](bughunter/mcp/caido-mcp-client/) |
| HackerOne MCP | Public HackerOne API and Hacktivity intelligence helper | [`bughunter/mcp/hackerone-mcp/`](bughunter/mcp/hackerone-mcp/) |

---

## Repository Structure

```text
Break-The-Limit/
├── assets/          # Project banner (assets/banner.png)
├── bughunter/       # Core breach CLI engine, multi-provider brain, skill loader, chat agent, tools, MCP
├── skills/          # 25 Break-The-Limit tactical offensive security playbooks
├── commands/        # 42 slash command definitions (+ README.md)
├── hooks/           # Harness lifecycle hooks
├── rules/           # Hunting & reporting rules
├── scripts/         # Utility scripts
├── docs/            # Guides & verified model catalog
└── tests/           # Automated test suite (pytest)
```

---

## Disclaimer

Break-The-Limit is developed and provided strictly for educational purposes, authorized bug bounty hunting, and lawful security research.

- **No Liability:** The authors and contributors assume no liability and are not responsible for any misuse, system damage, data loss, or unlawful activity conducted with this software.
- **Authorized Use Only:** You may only use this toolkit against systems, applications, and networks for which you have explicit written permission or that fall within the published scope of an authorized bug bounty program.
- **User Responsibility:** The end user bears full legal responsibility for ensuring all testing complies with applicable local and international laws.

---

## License

Licensed under the MIT License — see [LICENSE](LICENSE).
