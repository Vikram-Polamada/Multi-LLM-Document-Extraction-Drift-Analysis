# Multi-LLM-Document-Extraction-Drift-Analysis
A production-style AI pipeline that extracts structured information from documents using multiple Large Language Models, compares their outputs, detects drift, and auto-corrects schema inconsistencies.

Overview:-

This project:
📂 Loads documents (PDF, DOCX, TXT)
🤖 Extracts structured JSON using multiple LLMs
🔍 Compares outputs across models
📊 Calculates a Drift Score
🛠 Auto-corrects schema mismatches

It helps evaluate consistency, reliability, and agreement between different LLMs.

🧠 Models Used
OpenAI GPT-4.1 Mini
Google Gemini 1.5 Flash
Anthropic Claude 3.5 Sonnet

Project Structure:-
.
├── main.py
├── document_loader.py
├── llm_clients.py
├── compare_engine.py
├── autocorrect_engine.py
├── schema.json
└── sample.pdf

Use Cases:-

Multi-LLM benchmarking
AI reliability testing
Structured document intelligence
Research on model agreement
Schema enforcement pipelines
