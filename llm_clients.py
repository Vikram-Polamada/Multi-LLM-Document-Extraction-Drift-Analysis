from openai import OpenAI
import google.generativeai as genai
import anthropic
import json

# ==============================
# INSERT YOUR API KEYS
# ==============================

OPENAI_KEY = "YOUR_OPENAI_KEY"
GEMINI_KEY = "YOUR_GEMINI_KEY"
CLAUDE_KEY = "YOUR_CLAUDE_KEY"


# ==============================
# INITIALIZE CLIENTS
# ==============================

client_openai = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None
genai.configure(api_key=GEMINI_KEY) if GEMINI_KEY else None
client_claude = anthropic.Anthropic(api_key=CLAUDE_KEY) if CLAUDE_KEY else None


# ==============================
# PROMPT TEMPLATE
# ==============================

SCHEMA_PROMPT = """
Extract structured information from the following document.

Return ONLY valid JSON in this exact schema:

{
  "title": "string",
  "author": "string",
  "date": "string",
  "key_points": ["string"],
  "summary": "string"
}

Document:
{}
"""


# ==============================
# MODEL FUNCTIONS
# ==============================

def call_chatgpt(text):
    if not client_openai:
        return {"error": "OpenAI API key missing"}

    res = client_openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": SCHEMA_PROMPT.format(text)}],
        temperature=0
    )
    return json.loads(res.choices[0].message.content)


def call_gemini(text):
    if not GEMINI_KEY:
        return {"error": "Gemini API key missing"}

    model = genai.GenerativeModel("gemini-1.5-flash")
    res = model.generate_text(SCHEMA_PROMPT.format(text))
    return json.loads(res.text)


def call_claude(text):
    if not client_claude:
        return {"error": "Claude API key missing"}

    res = client_claude.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=500,
        messages=[{"role": "user", "content": SCHEMA_PROMPT.format(text)}]
    )
    return json.loads(res.content[0].text)
