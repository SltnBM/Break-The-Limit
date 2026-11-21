<p align="center">
  <img src="assets/banner.png" alt="Break-The-Limit — Unified AI-Powered Bug Bounty & Security Research Toolkit" width="100%"/>
</p>

<h1 align="center">Break-The-Limit</h1>

<p align="center">
  <b>Unified AI-powered bug bounty &amp; security research toolkit — recon to report, in your terminal.</b>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Skills-99-00C853.svg?style=flat-square" alt="99 Skills">
  <img src="https://img.shields.io/badge/Commands-43-7C4DFF.svg?style=flat-square" alt="43 Commands">
  <img src="https://img.shields.io/badge/Tests-1216_passed-00B0FF.svg?style=flat-square" alt="Tests">
</p>

---

## Overview

**Break-The-Limit** is a unified, terminal-native bug bounty hunting and offensive security research framework. It brings together:

- **`bughunter` CLI** — Interactive AI hunting assistant (`bughunter chat` with Phase 0–5 workflow, `--phase` / `--target` resume, network/tool execution, Google OAuth / Antigravity `agy`, Custom Providers, Ollama, Groq, OpenAI, Anthropic, and DeepSeek).
- **`cbh` CLI & Engine** — Recon classification, triage, and reporting runner with ledger-backed state management.
- **99 Specialized Security Skills (`skills/`)** — Modular playbooks covering Web2, API, GraphQL, Auth/OAuth/SAML/MFA, Cloud IAM (AWS/GCP/Azure), M365/Entra, Okta, Kubernetes, CI/CD, Mobile (APK/iOS), LLM/RAG/MCP security, Web3/DeFi, OSINT, and report writing.
- **43 Slash Commands (`commands/`)** — Ready-to-use workflows (`/recon`, `/hunt`, `/validate`, `/report`, `/chain`, `/scope`, `/triage`, `/autopilot`, `/surface`, `/web3-audit`, and more).
- **MCP Integrations (`mcp/`, `bughunter/mcp/`)** — Adapters for HackerOne, Burp Suite, Caido, and tool-policy enforcement.

---

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/SltnBM/Break-The-Limit.git
cd Break-The-Limit
pip install -e ".[test]"
```

Optional: install harness skills/commands/agents for Claude Code, OpenCode, Pi, or Codex:

```bash
chmod +x install.sh && ./install.sh
```

### 2. Configure Provider (`bughunter setup`)

```bash
bughunter setup
```

Supported providers include:
- **Google OAuth / Antigravity (`agy`)** — Use your Gemini AI Pro subscription without an API key
- **Custom Provider** — Point to any OpenAI-compatible endpoint (e.g. `9router`, local vLLM/LM Studio)
- **Local / Cloud APIs** — Ollama, Groq, OpenRouter, DeepSeek, Anthropic, OpenAI

Check available models anytime:

```bash
bughunter models
```

### 3. Start Hunting (`bughunter chat`)

```bash
# Interactive Phase 0-5 guided bug hunting
bughunter chat

# Jump directly to a specific phase and target
bughunter chat --target example.com --phase 3
```

---

## Structured Hunting Workflow (Phase 0 – Phase 5)

| Phase | Focus |
|---|---|
| **Phase 0** | Scope verification & rules of engagement |
| **Phase 1** | Reconnaissance & asset discovery (`subfinder`, `httpx`, `katana`, JS/endpoint mapping) |
| **Phase 2** | Attack surface ranking & lead prioritization |
| **Phase 3** | Targeted vulnerability hunting (IDOR, Auth/OAuth, SSRF, SQLi, XSS, Business Logic, etc.) |
| **Phase 4** | Validation & 7-Question Gate (eliminate false positives before reporting) |
| **Phase 5** | PoC bundling, CVSS 3.1 scoring, and submission-ready reporting |

---

## Repository Structure

```text
Break-The-Limit/
├── bughunter/       # Core bughunter CLI, chat agent, OAuth/providers, tools, memory, MCP
├── cbh/             # cbh CLI package for recon/classify/triage/report
├── engine/          # Ledger & state engine
├── skills/          # 99 domain-specific security & hunting skills
├── commands/        # 43 slash command workflows
├── hooks/           # Harness hooks
├── rules/           # Always-active hunting & reporting rules
├── mcp/             # MCP server adapters (HackerOne, Burp, Caido)
├── scripts/         # Utility & bootstrap scripts
├── docs/            # Architecture, CLI, verification & methodology docs
└── tests/           # Automated test suite (pytest)
```

---

## Running Tests

```bash
pytest -q
```

---

## License & Disclaimer

Licensed under the **MIT License** — see [LICENSE](LICENSE).

> **Authorized Testing Only:** Break-The-Limit is built for authorized bug bounty hunting, security research, and penetration testing within explicitly approved scope. Never test targets without permission.
