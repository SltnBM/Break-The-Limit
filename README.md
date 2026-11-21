<p align="center">
  <img src="assets/banner.png" alt="Break-The-Limit" width="100%"/>
</p>

<h1 align="center">Break-The-Limit</h1>

<p align="center">
  Terminal-native AI bug bounty &amp; security research toolkit — recon to report.
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

Break-The-Limit menggabungkan CLI agent interaktif, runner deterministik, playbook kerentanan, dan integrasi MCP dalam satu repositori.

| Component | Fungsi | Path |
|---|---|---|
| `breach` CLI | Agent hunting interaktif dan pipeline Phase 0–5 | [`bughunter/`](bughunter/) |
| `cbh` CLI | Runner recon, klasifikasi, triage, dan laporan | [`cbh/`](cbh/) |
| Ledger Engine | State management dan penyimpanan data hunt | [`engine/`](engine/) |
| 99 Security Skills | Playbook kerentanan per domain target | [`skills/`](skills/) |
| 42 Slash Commands | Alur kerja terstruktur untuk harness AI | [`commands/`](commands/) |
| MCP Integrations | Adapter server MCP untuk proxy dan platform | [`bughunter/mcp/`](bughunter/mcp/) |
| 1,216 Automated Tests | Verifikasi unit, skema, dan path tool | [`tests/`](tests/) |

---

## Quick Start

Install paket Python, pasang skill ke harness pilihan, lalu konfigurasi provider AI dan verifikasi test suite.

```bash
git clone https://github.com/SltnBM/Break-The-Limit.git
cd Break-The-Limit
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"

# Alternatif global tanpa virtualenv:
# ./install.sh --agent standalone

# Opsional: pasang skill ke harness (Claude Code / OpenCode / Codex)
chmod +x install.sh
./install.sh --agent all

# Konfigurasi provider AI dan verifikasi instalasi
breach setup
pytest -q
```

---

## Usage

### Core Commands

Gunakan perintah berikut sesuai alur dari setup awal hingga verifikasi test.

| Task | Command |
|---|---|
| Konfigurasi provider AI | `breach setup` |
| Lihat daftar model aktif | `breach models` |
| Mulai sesi hunting interaktif | `breach chat` |
| Lanjutkan target pada phase tertentu | `breach chat --target example.com --phase 3` |
| Jalankan pipeline hunt otomatis | `breach hunt example.com` |
| Jalankan runner CLI deterministik | `cbh --help` |
| Jalankan seluruh test suite | `pytest -q` |

### Phase 0–5 Workflow

Sesi `breach chat` membagi proses audit menjadi enam tahap berurutan.

| Phase | Tujuan |
|---|---|
| `0 · Scope` | Memverifikasi domain in-scope dan batasan program sebelum pengujian |
| `1 · Reconnaissance` | Mengumpulkan subdomain, host aktif, endpoint, dan fingerprint teknologi |
| `2 · Surface Ranking` | Memprioritaskan endpoint dan alur bernilai tinggi dari hasil recon |
| `3 · Targeted Hunting` | Menguji celah spesifik pada target prioritas |
| `4 · Validation` | Menyaring false positive melalui 7-Question Gate |
| `5 · PoC & Reporting` | Menyusun bukti reproduksi dan draf laporan siap kirim |

---

## Supported AI Providers

Pilih provider lokal, OAuth, API key, gateway, atau endpoint kustom; lihat daftar model terverifikasi di [Supported AI Models](docs/supported-models.md).

### Subscription / OAuth

| Provider | Auth | Catatan |
|---|---|---|
| `antigravity` (`agy`) | OAuth | Gemini AI Pro via Google OAuth |
| `gemini-oauth` | OAuth | Kredensial Google OAuth CLI |

### Local

| Provider | Auth | Catatan |
|---|---|---|
| `ollama` | Local | Gratis, offline via `OLLAMA_HOST` |

### Cloud API

| Provider | Auth | Catatan |
|---|---|---|
| `groq` | API key | `GROQ_API_KEY`, free tier cepat |
| `cerebras` | API key | `CEREBRAS_API_KEY`, inferensi berkecepatan tinggi |
| `deepseek` | API key | `DEEPSEEK_API_KEY`, model V4 hemat biaya |
| `gemini` | API key | `GEMINI_API_KEY`, Google Gemini API |
| `claude` | API key | `ANTHROPIC_API_KEY`, Anthropic Claude API |
| `openai` | API key | `OPENAI_API_KEY`, OpenAI API |
| `grok` | API key | `XAI_API_KEY`, xAI Grok API |
| `kimi` | API key | `MOONSHOT_API_KEY`, Moonshot AI API |
| `mistral` | API key | `MISTRAL_API_KEY`, Mistral AI API |
| `together` | API key | `TOGETHER_API_KEY`, model open-weight cloud |
| `perplexity` | API key | `PERPLEXITY_API_KEY`, pencarian web terintegrasi |

### Gateway & Custom

| Provider | Auth | Catatan |
|---|---|---|
| `openrouter` | API key | `OPENROUTER_API_KEY`, multi-model gateway |
| `orcarouter` | API key | `ORCAROUTER_API_KEY`, multi-model gateway |
| `fluxion` | API key | `FLUXION_API_KEY`, multi-model gateway |
| `requesty` | API key | `REQUESTY_API_KEY`, multi-model gateway |
| `litellm` | API key | `LITELLM_API_KEY`, gateway 100+ provider |
| `custom` | Custom URL | `CUSTOM_BASE_URL`, OpenAI-compatible server |

---

## Skills & Commands

### Skills (99)

Playbook dikelompokkan ke dalam enam domain keamanan.

| Domain | Jumlah | Contoh |
|---|---|---|
| Methodology & Reporting | 14 | `bb-methodology`, `triage-validation`, `report-writing`, `evidence-hygiene`, [semua →](skills/) |
| Web & API | 37 | `hunt-idor`, `hunt-ssrf`, `hunt-sqli`, `hunt-xss`, [semua →](skills/) |
| Auth & Identity | 13 | `hunt-ato`, `hunt-oauth`, `hunt-saml`, `hunt-jwt-crypto`, [semua →](skills/) |
| Cloud, Infra & Stacks | 18 | `hunt-cloud-misconfig`, `cloud-iam-deep`, `hunt-k8s`, `hunt-cicd`, [semua →](skills/) |
| AI, LLM & Web3 | 9 | `hunt-llm-ai`, `mcp-server-audit`, `web3-audit`, `meme-coin-audit`, [semua →](skills/) |
| Mobile & OSINT | 8 | `apk-redteam-pipeline`, `ios-redteam-pipeline`, `osint-methodology`, `web2-recon`, [semua →](skills/) |

<details>
<summary>Methodology &amp; Reporting (14)</summary>

| Skill | Skill |
|---|---|
| `bb-local-toolkit` | `mid-engagement-ir-detection` |
| `bb-methodology` | `omni-killchain` |
| `bug-bounty` | `redteam-mindset` |
| `bug-chaining` | `redteam-report-template` |
| `bugcrowd-reporting` | `report-writing` |
| `evidence-hygiene` | `security-arsenal` |
| `hunt-dispatch` | `triage-validation` |

</details>

<details>
<summary>Web &amp; API (37)</summary>

| Skill | Skill |
|---|---|
| `client-reverse` | `hunt-idor` |
| `graphql-audit` | `hunt-ldap` |
| `hunt-api-misconfig` | `hunt-lfi` |
| `hunt-business-logic` | `hunt-misc` |
| `hunt-cache-poison` | `hunt-nosqli` |
| `hunt-captcha-bypass` | `hunt-open-redirect` |
| `hunt-clickjacking` | `hunt-race-condition` |
| `hunt-cors` | `hunt-rce` |
| `hunt-csrf` | `hunt-shadow-api` |
| `hunt-deserialization` | `hunt-spa-api` |
| `hunt-dom` | `hunt-sqli` |
| `hunt-exceptional-conditions` | `hunt-ssrf` |
| `hunt-file-upload` | `hunt-ssti` |
| `hunt-fintech-graphql` | `hunt-websocket` |
| `hunt-graphql` | `hunt-xss` |
| `hunt-grpc` | `hunt-xxe` |
| `hunt-host-header` | `jsmax` |
| `hunt-html-injection` | `web2-vuln-classes` |
| `hunt-http-smuggling` | |

</details>

<details>
<summary>Auth &amp; Identity (13)</summary>

| Skill | Skill |
|---|---|
| `credential-attack` | `hunt-ntlm-info` |
| `hunt-ato` | `hunt-oauth` |
| `hunt-auth-bypass` | `hunt-saml` |
| `hunt-brute-force` | `hunt-session` |
| `hunt-forgot-password` | `m365-entra-attack` |
| `hunt-jwt-crypto` | `okta-attack` |
| `hunt-mfa-bypass` | |

</details>

<details>
<summary>Cloud, Infra &amp; Stacks (18)</summary>

| Skill | Skill |
|---|---|
| `cicd-security` | `hunt-laravel` |
| `cloud-iam-deep` | `hunt-nextjs` |
| `cloud-pentest` | `hunt-nodejs` |
| `enterprise-vpn-attack` | `hunt-sharepoint` |
| `hunt-aspnet` | `hunt-source-leak` |
| `hunt-cicd` | `hunt-springboot` |
| `hunt-cloud-misconfig` | `hunt-subdomain` |
| `hunt-k8s` | `hunt-tls-network` |
| `supply-chain-attack-recon` | `vmware-vcenter-attack` |

</details>

<details>
<summary>AI, LLM &amp; Web3 (9)</summary>

| Skill | Skill |
|---|---|
| `agentic-app-audit` | `llm-redteam` |
| `argus` | `mcp-server-audit` |
| `hunt-llm-ai` | `meme-coin-audit` |
| `hunt-rag-vector` | `web3-audit` |
| `johnwick` | |

</details>

<details>
<summary>Mobile &amp; OSINT (8)</summary>

| Skill | Skill |
|---|---|
| `apk-redteam-pipeline` | `osint-methodology` |
| `ios-redteam-pipeline` | `pii-hunter` |
| `mobile-pentest` | `recon-scope-triage` |
| `offensive-osint` | `web2-recon` |

</details>

### Commands (42)

Dua belas slash command utama ditunjukkan di bawah ini, dan daftar lengkap 42 command tersedia di bagian lipat.

| Kategori | Command | Fungsi |
|---|---|---|
| Recon | `/recon` | Jalankan pipeline recon lengkap |
| Recon | `/scope` | Verifikasi aset terhadap scope program |
| Recon | `/surface` | Urutkan prioritas attack surface target |
| Hunt | `/hunt` | Jalankan pengujian kerentanan aktif |
| Hunt | `/autopilot` | Jalankan loop hunt otomatis |
| Hunt | `/chain` | Rangkai beberapa temuan menjadi eskalasi |
| Validate & Report | `/validate` | Jalankan 7-Question Gate pada temuan |
| Validate & Report | `/triage` | Evaluasi cepat kelayakan temuan |
| Validate & Report | `/report` | Buat draf laporan siap kirim |
| Utilities | `/pickup` | Lanjutkan sesi hunt sebelumnya |
| Web3 & OSINT | `/web3-audit` | Audit smart contract Solidity/Rust |
| Web3 & OSINT | `/token-scan` | Pindai risiko rug pull token |

<details>
<summary>Daftar lengkap 42 Slash Commands (<code>commands/</code>)</summary>

| Kategori | Command | Fungsi |
|---|---|---|
| Recon | `/recon` | Jalankan pipeline recon lengkap |
| Recon | `/scope` | Verifikasi aset terhadap scope program |
| Recon | `/scope-aggregate` | Kumpulkan scope dari berbagai platform |
| Recon | `/surface` | Urutkan prioritas attack surface target |
| Recon | `/cloud-recon` | Cari bucket publik dan origin IP |
| Recon | `/param-discover` | Temukan parameter HTTP tersembunyi |
| Recon | `/secrets-hunt` | Pindai kebocoran kredensial di kode |
| Recon | `/takeover` | Periksa kandidat subdomain takeover |
| Recon | `/portscan` | Pindai port layanan pada target |
| Recon | `/intel` | Ambil data CVE dan laporan publik |
| Hunt | `/hunt` | Jalankan pengujian kerentanan aktif |
| Hunt | `/autopilot` | Jalankan loop hunt otomatis |
| Hunt | `/chain` | Rangkai beberapa temuan menjadi eskalasi |
| Hunt | `/bypass-403` | Uji teknik bypass HTTP 403/401 |
| Hunt | `/cors` | Pindai kesalahan konfigurasi CORS |
| Hunt | `/crlf` | Uji CRLF dan host header injection |
| Hunt | `/domxss` | Konfirmasi DOM XSS di browser |
| Hunt | `/jwt-scan` | Analisis dan uji token JWT offline |
| Hunt | `/nosqli` | Pindai celah injeksi NoSQL |
| Hunt | `/oob` | Korelasi callback out-of-band interactsh |
| Hunt | `/scan-cves` | Sapuan template Nuclei untuk CVE |
| Hunt | `/sast` | Jalankan aturan Semgrep pada source |
| Hunt | `/llm-app-audit` | Audit black-box aplikasi agen AI |
| Hunt | `/llm-redteam` | Uji prompt injection dan jailbreak |
| Hunt | `/spray` | Password spray dengan pengaman lockout |
| Validate & Report | `/validate` | Jalankan 7-Question Gate pada temuan |
| Validate & Report | `/triage` | Evaluasi cepat kelayakan temuan |
| Validate & Report | `/verify` | Verifikasi ulang bundle PoC secara independen |
| Validate & Report | `/report` | Buat draf laporan siap kirim |
| Validate & Report | `/poc` | Susun template bukti reproduksi PoC |
| Validate & Report | `/screenshot` | Ambil tangkapan layar daftar host aktif |
| Validate & Report | `/remember` | Simpan temuan ke memori hunt |
| Utilities | `/arsenal` | Daftar tool eksternal yang terpasang |
| Utilities | `/dashboard` | Buka dashboard lokal hasil hunt |
| Utilities | `/memory-gc` | Rotasi dan bersihkan log memori |
| Utilities | `/oracle` | Urutkan prioritas lead berbasis histori |
| Utilities | `/pickup` | Lanjutkan sesi hunt sebelumnya |
| Web3 & OSINT | `/web3-audit` | Audit smart contract Solidity/Rust |
| Web3 & OSINT | `/token-scan` | Pindai risiko rug pull token |
| Web3 & OSINT | `/wordlist-gen` | Buat wordlist khusus dari situs target |
| Web3 & OSINT | `/osint-employees` | Kumpulkan OSINT nama dan email karyawan |
| Web3 & OSINT | `/breach-check` | Cek wordlist terhadap API HIBP |

</details>

---

## MCP Integrations

Server dan klien MCP berikut menghubungkan agent ke proxy HTTP serta API platform bug bounty.

| Integration | Fungsi | Path |
|---|---|---|
| Break-The-Limit MCP | Server MCP lokal dengan redaksi otomatis | [`bughunter/mcp/bughunter-mcp/`](bughunter/mcp/bughunter-mcp/) |
| Burp Suite MCP Client | Klien bridge untuk proxy Burp Suite | [`bughunter/mcp/burp-mcp-client/`](bughunter/mcp/burp-mcp-client/) |
| Caido MCP Client | Klien bridge untuk proxy Caido | [`bughunter/mcp/caido-mcp-client/`](bughunter/mcp/caido-mcp-client/) |
| HackerOne MCP | Helper API publik HackerOne dan Hacktivity | [`bughunter/mcp/hackerone-mcp/`](bughunter/mcp/hackerone-mcp/) |
| HackerOne MCP Adapter | Adapter MCP tambahan untuk HackerOne | [`mcp/hackerone/`](mcp/hackerone/) |

---

## Repository Structure

```text
Break-The-Limit/
├── bughunter/       # Core CLI, chat agent, OAuth/providers, tools, memory, MCP
├── cbh/             # Terminal-native deterministic CLI runner
├── engine/          # State & ledger engine
├── skills/          # 99 domain-specific security playbooks
├── commands/        # 42 slash command definitions (+ README.md)
├── hooks/           # Harness lifecycle hooks
├── rules/           # Hunting & reporting rules
├── mcp/             # Standalone MCP adapters
├── scripts/         # Installers & helper scripts
├── docs/            # Guides, schemas & model catalog
└── tests/           # 1,216 automated tests (pytest)
```

---

## Disclaimer

Break-The-Limit dikembangkan dan disediakan hanya untuk tujuan edukasi, bug bounty resmi, dan riset keamanan yang sah.

- **No Liability:** Penulis dan kontributor tidak bertanggung jawab atas penyalahgunaan, kerusakan sistem, kehilangan data, atau aktivitas ilegal yang dilakukan menggunakan perangkat lunak ini.
- **Authorized Use Only:** Perangkat ini hanya boleh digunakan terhadap sistem, aplikasi, dan jaringan yang memiliki izin tertulis resmi atau termasuk dalam cakupan program bug bounty yang sah.
- **User Responsibility:** Pengguna bertanggung jawab penuh memastikan seluruh aktivitas mematuhi hukum dan peraturan yang berlaku.

---

## License

Licensed under the MIT License — see [LICENSE](LICENSE).
