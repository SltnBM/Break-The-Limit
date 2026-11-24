# Supported AI Models

Verified default models and catalog labels sourced directly from [`bughunter/brain.py`](../bughunter/brain.py) and [`bughunter/tools/google_oauth.py`](../bughunter/tools/google_oauth.py).

## Antigravity / Gemini OAuth (`agy`)

The following models are defined in `ANTIGRAVITY_MODEL_LABELS` in [`bughunter/tools/google_oauth.py`](../bughunter/tools/google_oauth.py):

- `gemini-4-argon-high`, `gemini-4-argon-medium`, `gemini-4-argon-low`
- `gemini-4-hydrogen-xhigh`, `gemini-4-hydrogen-high`, `gemini-4-hydrogen-medium`, `gemini-4-hydrogen-low`
- `gemini-3.8-flash-high`, `gemini-3.8-flash-medium`, `gemini-3.8-flash-low`
- `claude-sonnet-5-5-high`, `claude-sonnet-5-5-medium`, `claude-sonnet-5-5-low`
- `claude-opus-5-5-high`, `claude-opus-5-5-medium`, `claude-opus-5-5-low`
- `gpt-oss-120b-medium`

To list live models from your active provider, run:

```bash
breach models
```

## Default Models per Provider

The following defaults are registered in `LLMClient.DEFAULT_MODELS` in [`bughunter/brain.py`](../bughunter/brain.py):

| Provider | Env Var / Endpoint | Default Model |
|---|---|---|
| `antigravity` (`agy`) | Google OAuth | `gemini-3.8-flash-medium` |
| `gemini-oauth` | Google OAuth CLI | `gemini-3.8-flash-medium` |
| `9router` / `custom` | `CUSTOM_BASE_URL` | Auto-discovered via `GET /v1/models` or user-specified |
| `ollama` | `OLLAMA_HOST` | Auto-discovered from local Ollama daemon |
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
| `requesty` | `REQUESTY_API_KEY` | `anthropic/claude-sonnet-4.6` |
| `litellm` | `LITELLM_API_KEY` | `gpt-4o` |
