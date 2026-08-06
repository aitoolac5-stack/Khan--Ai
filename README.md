# Alpha AI ✦

A polished, responsive AI assistant with a secure server-side model integration.

## Features

- Modern responsive chat interface
- Conversation history sent to the model for contextual replies
- New-chat reset
- Enter to send / Shift+Enter for a new line
- Server-side API key handling
- Configurable OpenAI-compatible model endpoint
- Health endpoint for deployment checks
- Input/history limits to reduce accidental oversized requests

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Set `AI_API_KEY` in `.env`. Optional variables:

- `AI_API_BASE_URL` — defaults to `https://api.openai.com/v1`
- `AI_MODEL` — defaults to `gpt-4o-mini`
- `PORT` — defaults to `5000`

**Never commit a real API key.**

## Important

Alpha AI is an application layer, not a newly trained foundation model. Its intelligence comes from the configured model provider. The repository is structured so the provider can be changed without exposing credentials to the browser.
