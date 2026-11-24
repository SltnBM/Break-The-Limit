"""Native Skill Engine for Break-The-Limit (`breach`).

Discovers, searches, recommends, and injects tactical playbooks from `skills/*/SKILL.md`
directly into the `breach` CLI and interactive `breach chat` sessions across any AI provider.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = REPO_ROOT / "skills"

# Backward-compatible aliases mapping legacy skill names to Break-The-Limit skill names
LEGACY_SKILL_ALIASES: dict[str, str] = {
    "agentic-app-audit": "agentic-system-audit",
    "argus": "taint-trace-audit",
    "bb-methodology": "btl-methodology",
    "bug-bounty": "btl-master-hunt",
    "bug-chaining": "exploit-chaining",
    "bugcrowd-reporting": "vrt-triage-reporting",
    "cicd-security": "pipeline-exploitation",
    "client-reverse": "client-js-reverse",
    "cloud-pentest": "cloud-post-exploit",
    "credential-attack": "cred-spray-ops",
    "graphql-audit": "graphql-offensive",
    "johnwick": "business-logic-assault",
    "jsmax": "js-deep-miner",
    "llm-redteam": "ai-prompt-redteam",
    "mcp-server-audit": "mcp-security-audit",
    "meme-coin-audit": "token-rugpull-audit",
    "mobile-pentest": "mobile-runtime-audit",
    "omni-killchain": "zero-day-killchain",
    "pii-hunter": "pii-exposure-hunter",
    "report-writing": "bounty-reporting",
    "security-arsenal": "payload-arsenal",
    "triage-validation": "impact-gate",
    "web2-recon": "surface-recon",
    "web2-vuln-classes": "web-exploit-matrix",
    "web3-audit": "defi-contract-audit",
}

SKILL_DOMAINS: dict[str, str] = {
    "btl-methodology": "Core Methodology",
    "btl-master-hunt": "Core Methodology",
    "impact-gate": "Validation & Triage",
    "bounty-reporting": "Reporting",
    "vrt-triage-reporting": "Reporting",
    "exploit-chaining": "Exploit Chaining",
    "surface-recon": "Recon & OSINT",
    "web-exploit-matrix": "Web & API",
    "payload-arsenal": "Web & API",
    "graphql-offensive": "Web & API",
    "business-logic-assault": "Web & API",
    "zero-day-killchain": "Web & API",
    "taint-trace-audit": "Code & Client Analysis",
    "client-js-reverse": "Code & Client Analysis",
    "js-deep-miner": "Code & Client Analysis",
    "pii-exposure-hunter": "Recon & OSINT",
    "cred-spray-ops": "Auth & Identity",
    "cloud-post-exploit": "Cloud & CI/CD",
    "pipeline-exploitation": "Cloud & CI/CD",
    "mobile-runtime-audit": "Mobile",
    "ai-prompt-redteam": "AI & MCP",
    "agentic-system-audit": "AI & MCP",
    "mcp-security-audit": "AI & MCP",
    "defi-contract-audit": "Web3 & Token",
    "token-rugpull-audit": "Web3 & Token",
}

SIGNAL_RECOMMENDATIONS: list[tuple[tuple[str, ...], str, str]] = [
    (("graphql", "/graphql", "gql", "introspection"), "graphql-offensive", "GraphQL endpoint / schema signals"),
    (("js", "webpack", "sourcemap", ".js.map", "bundle"), "js-deep-miner", "JavaScript bundle & endpoint mining"),
    (("reverse", "obfuscat", "wasm", "crypto", "signature"), "client-js-reverse", "Client-side JS reverse engineering"),
    (("idor", "bola", "ssrf", "xss", "sqli", "oauth", "cors"), "web-exploit-matrix", "Web & API vulnerability classes"),
    (("logic", "race", "coupon", "payment", "checkout", "ato"), "business-logic-assault", "High-impact business logic & state abuse"),
    (("chain", "escalat", "low to critical"), "exploit-chaining", "Multi-bug A->B->C exploit chaining"),
    (("0day", "killchain", "deserial", "smuggl", "cache"), "zero-day-killchain", "Full-spectrum multi-stage exploitation"),
    (("sast", "source", "sink", "taint", "repo", "code"), "taint-trace-audit", "Source-to-sink taint & code analysis"),
    (("pii", "leak", "gdpr", "dump", "exposure"), "pii-exposure-hunter", "Sensitive PII & data exposure hunting"),
    (("recon", "subdomain", "subfinder", "httpx", "surface"), "surface-recon", "Attack surface discovery & live probing"),
    (("aws", "gcp", "azure", "iam", "s3", "imds", "cloud"), "cloud-post-exploit", "Cloud IAM & post-access exploitation"),
    (("github", "actions", "cicd", "pipeline", "runner"), "pipeline-exploitation", "CI/CD workflow & runner exploitation"),
    (("apk", "ios", "ipa", "frida", "mobile", "android"), "mobile-runtime-audit", "Mobile app decompilation & runtime hooking"),
    (("llm", "prompt", "jailbreak", "chatbot", "ai"), "ai-prompt-redteam", "LLM prompt injection & guardrail testing"),
    (("agent", "tool call", "rag", "memory poison"), "agentic-system-audit", "Deployed AI agent & tool-hijack audit"),
    (("mcp", "model context protocol"), "mcp-security-audit", "MCP server tool poisoning & sink audit"),
    (("solidity", "defi", "foundry", "smart contract", "erc"), "defi-contract-audit", "Smart contract & DeFi protocol audit"),
    (("meme", "solana", "spl", "rug", "pump", "raydium"), "token-rugpull-audit", "Token authority & rug-pull detection"),
    (("spray", "password", "hibp", "breach", "okta", "o365"), "cred-spray-ops", "Password spray & breach correlation"),
    (("payload", "bypass", "waf", "wordlist"), "payload-arsenal", "Payloads & WAF bypass reference"),
    (("triage", "validate", "gate", "severity", "cvss"), "impact-gate", "7-Question Gate finding validation"),
    (("report", "hackerone", "intigriti", "immunefi"), "bounty-reporting", "Submission-ready report templates"),
    (("bugcrowd", "vrt"), "vrt-triage-reporting", "Bugcrowd VRT & downgrade counter tactics"),
]


def resolve_skill_name(name: str) -> str:
    """Normalize skill name and resolve legacy aliases."""
    clean = (name or "").strip().lower().lstrip("/")
    return LEGACY_SKILL_ALIASES.get(clean, clean)


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Extract YAML frontmatter key-values and return (meta, body)."""
    meta: dict[str, str] = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_raw = parts[1]
            body = parts[2].strip()
            for line in fm_raw.splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip().lower()] = v.strip().strip("\"'")
    return meta, body


def list_skills(skills_dir: Path | None = None) -> list[dict[str, Any]]:
    """Return metadata for all installed Break-The-Limit skills."""
    root = skills_dir or SKILLS_DIR
    if not root.is_dir():
        return []

    items: list[dict[str, Any]] = []
    for entry in sorted(root.iterdir()):
        skill_md = entry / "SKILL.md"
        if not entry.is_dir() or not skill_md.is_file():
            continue
        raw = skill_md.read_text(errors="replace")
        meta, body = _parse_frontmatter(raw)
        name = entry.name
        desc = meta.get("description", "").strip()
        if not desc:
            for line in body.splitlines():
                s = line.strip()
                if s and not s.startswith("#"):
                    desc = s
                    break
        items.append({
            "name": name,
            "domain": SKILL_DOMAINS.get(name, "Security Playbook"),
            "description": desc[:160] + ("..." if len(desc) > 160 else ""),
            "path": str(skill_md.relative_to(REPO_ROOT)) if skill_md.is_relative_to(REPO_ROOT) else str(skill_md),
        })
    return items


def load_skill(name: str, skills_dir: Path | None = None) -> dict[str, Any] | None:
    """Load a single skill by name (or legacy alias)."""
    root = skills_dir or SKILLS_DIR
    resolved = resolve_skill_name(name)
    skill_md = root / resolved / "SKILL.md"
    if not skill_md.is_file():
        return None
    raw = skill_md.read_text(errors="replace")
    meta, body = _parse_frontmatter(raw)
    return {
        "name": resolved,
        "domain": SKILL_DOMAINS.get(resolved, "Security Playbook"),
        "description": meta.get("description", ""),
        "body": body,
        "path": str(skill_md),
    }


def recommend_skills(query: str, limit: int = 5) -> list[dict[str, str]]:
    """Recommend relevant Break-The-Limit skills for a target technology, vuln class, or keyword."""
    q = (query or "").strip().lower()
    if not q:
        return [
            {"name": "btl-methodology", "reason": "Core non-linear hunting workflow"},
            {"name": "surface-recon", "reason": "Subdomain & live attack surface mapping"},
            {"name": "web-exploit-matrix", "reason": "26 Web & API vulnerability classes"},
        ]

    matches: list[dict[str, str]] = []
    seen: set[str] = set()
    for keywords, skill_name, reason in SIGNAL_RECOMMENDATIONS:
        if any(kw in q for kw in keywords) and skill_name not in seen:
            seen.add(skill_name)
            matches.append({"name": skill_name, "reason": reason})
            if len(matches) >= limit:
                return matches

    # Fallback substring search across skill names and descriptions
    for item in list_skills():
        if item["name"] in seen:
            continue
        if q in item["name"].lower() or q in item["description"].lower() or q in item["domain"].lower():
            seen.add(item["name"])
            matches.append({"name": item["name"], "reason": item["description"][:90]})
            if len(matches) >= limit:
                break
    return matches


def build_skill_prompt_context(
    skill_names: list[str],
    max_chars_per_skill: int = 4500,
    skills_dir: Path | None = None,
) -> tuple[str, list[str]]:
    """Build an injectable system-prompt block from one or more skill names.

    Returns (formatted_context_block, loaded_skill_names).
    """
    loaded_names: list[str] = []
    sections: list[str] = []

    for raw_name in skill_names:
        info = load_skill(raw_name, skills_dir=skills_dir)
        if not info:
            continue
        sname = info["name"]
        if sname in loaded_names:
            continue
        loaded_names.append(sname)
        body = info["body"].strip()
        if len(body) > max_chars_per_skill:
            body = body[:max_chars_per_skill] + "\n... [skill playbook truncated for context efficiency]"
        sections.append(
            f"### Active Tactical Skill: `{sname}` ({info['domain']})\n"
            f"{body}"
        )

    if not sections:
        return "", []

    header = (
        "Loaded Break-The-Limit Tactical Playbooks (apply these methodologies, payloads, "
        "and verification gates directly to the operator's requests):\n\n"
    )
    return header + "\n\n---\n\n".join(sections), loaded_names
