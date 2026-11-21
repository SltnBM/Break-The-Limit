<p align="center">
  <img src="assets/banner.png" alt="Break-The-Limit — Unified AI-Powered Bug Bounty & Security Research Toolkit" width="100%"/>
</p>

<h1 align="center">Break-The-Limit</h1>

<p align="center">
  <b>Unified AI-powered bug bounty &amp; security research toolkit — recon to report, in your terminal.</b>
</p>

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB.svg?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Skills-99-00C853.svg?style=flat-square" alt="99 Skills">
  <img src="https://img.shields.io/badge/Commands-43-7C4DFF.svg?style=flat-square" alt="43 Commands">
  <img src="https://img.shields.io/badge/Tests-1216_passed-00B0FF.svg?style=flat-square" alt="Tests">
</p>

---

## Overview

**Break-The-Limit** combines CLI automation, AI-assisted hunting, modular vulnerability playbooks, and MCP integrations into a single unified toolkit.

| Component | Description | Path |
|---|---|---|
| **`bughunter` CLI** | Interactive AI hunting assistant (`bughunter chat`), Phase 0–5 workflow, `--phase` / `--target` resume, OAuth & custom providers | [`bughunter/`](bughunter/) |
| **`cbh` CLI & Engine** | Recon classification, triage, and reporting runner backed by a persistent ledger engine | [`cbh/`](cbh/), [`engine/`](engine/) |
| **99 Security Skills** | Modular playbooks for Web2, API, GraphQL, Auth/OAuth/SAML/MFA, Cloud IAM, M365/Entra, Okta, K8s, CI/CD, Mobile, LLM/RAG/MCP, Web3 & OSINT | [`skills/`](skills/) |
| **43 Slash Commands** | Ready-to-use workflows (`/recon`, `/hunt`, `/validate`, `/report`, `/chain`, `/scope`, `/triage`, `/autopilot`, `/surface`, `/web3-audit`) | [`commands/`](commands/) |
| **MCP Integrations** | Adapters for HackerOne, Burp Suite, Caido, and tool-policy enforcement | [`mcp/`](mcp/), [`bughunter/mcp/`](bughunter/mcp/) |
| **Automated Tests** | Unit & integration test suite (`pytest`, 1,216+ tests) | [`tests/`](tests/) |

---

## Quick Start

```bash
git clone https://github.com/SltnBM/Break-The-Limit.git
cd Break-The-Limit
pip install -e ".[test]"

# Optional: install skills/commands/agents to Claude Code, OpenCode, Pi, or Codex
chmod +x install.sh && ./install.sh
```

---

## Usage Guide (Cara Pakai)

| Command / Workflow | Purpose | Example |
|---|---|---|
| **Setup AI Provider** | Configure Google OAuth (`agy`), Custom Provider, or API keys | `bughunter setup` |
| **Check Models** | List available models for the active provider | `bughunter models` |
| **Interactive AI Hunt** | Start Phase 0–5 guided bug hunting chat with tool execution | `bughunter chat` |
| **Resume by Phase** | Jump directly to a specific hunting phase (`0`–`5`) for a target | `bughunter chat --target example.com --phase 3` |
| **Autonomous / CLI Hunt** | Run recon, surface ranking, or full pipeline from CLI | `bughunter hunt example.com` |
| **`cbh` Runner** | Run `cbh` recon, classify, triage, and report commands | `cbh --help` |
| **Run Test Suite** | Verify local installation and tools | `pytest -q` |

### Structured Hunting Phases (Phase 0 – Phase 5)

| Phase | Focus |
|---|---|
| **Phase 0** | Scope verification & rules of engagement |
| **Phase 1** | Reconnaissance & asset discovery (`subfinder`, `httpx`, `katana`, JS/endpoint mapping) |
| **Phase 2** | Attack surface ranking & lead prioritization |
| **Phase 3** | Targeted vulnerability hunting (IDOR, Auth/OAuth, SSRF, SQLi, XSS, Business Logic, etc.) |
| **Phase 4** | Validation & 7-Question Gate (eliminate false positives before reporting) |
| **Phase 5** | PoC bundling, CVSS 3.1 scoring, and submission-ready reporting |

---

## Supported AI Providers (AI Support)

| Category | Provider | Auth / Setup | Default / Notes |
|---|---|---|---|
| **Google Subscription** | **Antigravity / Gemini OAuth (`agy`)** | Google OAuth (no API key) | `gemini-3.8-flash-medium` / `gemini-4-argon-high` / Claude via `agy` |
| **Custom Endpoint** | **Custom Provider** | Custom Base URL + optional key | Works with `9router`, local vLLM, LM Studio, or any OpenAI-compatible API |
| **Local (Zero Cost)** | **Ollama** | Local daemon (`ollama serve`) | Zero cost, runs local models (`qwen2.5`, `deepseek-r1`, etc.) |
| **Cloud Free / Fast** | **Groq**, **Cerebras** | `GROQ_API_KEY`, `CEREBRAS_API_KEY` | Fast inference (`openai/gpt-oss-20b`, etc.) |
| **Direct Model APIs** | **Gemini**, **Claude**, **OpenAI**, **DeepSeek**, **Grok**, **Mistral**, **Kimi** | Provider API Key | `gemini-3.8-flash-high`, `claude-sonnet`, `gpt-4o`, `deepseek-v4-flash` |
| **Multi-Model Gateways** | **OpenRouter**, **OrcaRouter**, **Together**, **Perplexity**, **Requesty** | Gateway API Key | Route to multiple frontier & open-weight models |

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

## Disclaimer

**Break-The-Limit** is developed and provided **strictly for educational purposes, authorized bug bounty hunting, and legitimate security research**.

- **No Liability:** The authors, maintainers, and contributors of **Break-The-Limit** are **not responsible or liable** for any misuse, damage, data loss, or illegal activities conducted using this toolkit or any of its components.
- **Authorized Use Only:** You may only use this project against systems, applications, and networks for which you have **explicit, written authorization** or that fall strictly within an **approved bug bounty program scope**.
- **User Responsibility:** End users are solely responsible for ensuring that their actions comply with all applicable local, national, and international laws and regulations.

---

## License

Licensed under the **MIT License** — see [LICENSE](LICENSE).
