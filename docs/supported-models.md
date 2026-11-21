# Supported AI Models

Daftar model default dan katalog model yang terverifikasi langsung dari kode (`bughunter/brain.py` dan `bughunter/tools/google_oauth.py`).

## Antigravity / Gemini OAuth (`agy`)

Model berikut terdaftar di `ANTIGRAVITY_MODEL_LABELS` pada [`bughunter/tools/google_oauth.py`](../bughunter/tools/google_oauth.py):

- `gemini-4-argon-high`, `gemini-4-argon-medium`, `gemini-4-argon-low`
- `gemini-4-hydrogen-xhigh`, `gemini-4-hydrogen-high`, `gemini-4-hydrogen-medium`, `gemini-4-hydrogen-low`
- `gemini-3.8-flash-high`, `gemini-3.8-flash-medium`, `gemini-3.8-flash-low`
- `claude-sonnet-5-5-high`, `claude-sonnet-5-5-medium`, `claude-sonnet-5-5-low`
- `claude-opus-5-5-high`, `claude-opus-5-5-medium`, `claude-opus-5-5-low`
- `gpt-oss-120b-medium`

Untuk melihat daftar model live dari CLI `agy`, jalankan:

```bash
breach models
```

## Default Models per Provider

Model default berikut terdaftar di `LLMClient.DEFAULT_MODELS` pada [`bughunter/brain.py`](../bughunter/brain.py):

| Provider | Env Var / Endpoint | Default Model |
|---|---|---|
| `antigravity` | Google OAuth (`agy`) | `gemini-3.8-flash-medium` |
| `gemini-oauth` | Google OAuth CLI | `gemini-3.8-flash-medium` |
| `ollama` | `OLLAMA_HOST` | Resolved dynamically from local daemon |
| `groq` | `GROQ_API_KEY` | `openai/gpt-oss-20b` |
| `cerebras` | `CEREBRAS_API_KEY` | `llama3.3-70b` |
| `deepseek` | `DEEPSEEK_API_KEY` | `deepseek-v4-flash` |
| `gemini` | `GEMINI_API_KEY` | `gemini-3.8-flash-high` |
| `claude` | `ANTHROPIC_API_KEY` | `claude-sonnet-4-6` |
| `openai` | `OPENAI_API_KEY` | `gpt-4o` |
| `grok` | `XAI_API_KEY` | `grok-4.5` |
| `kimi` | `MOONSHOT_API_KEY` | `moonshot-v1-128k` |
| `mistral` | `MISTRAL_API_KEY` | `mistral-large-latest` |
| `together` | `TOGETHER_API_KEY` | `meta-llama/Llama-3.3-70B-Instruct-Turbo` |
| `perplexity` | `PERPLEXITY_API_KEY` | `sonar-pro` |
| `openrouter` | `OPENROUTER_API_KEY` | `anthropic/claude-sonnet-4.6` |
| `orcarouter` | `ORCAROUTER_API_KEY` | `openai/gpt-4o` |
| `fluxion` | `FLUXION_API_KEY` | `openai/gpt-4o` |
| `requesty` | `REQUESTY_API_KEY` | `anthropic/claude-sonnet-4-6` |
| `litellm` | `LITELLM_API_KEY` | `gpt-4o` |
| `custom` | `CUSTOM_BASE_URL` | Resolved dynamically or from config |
