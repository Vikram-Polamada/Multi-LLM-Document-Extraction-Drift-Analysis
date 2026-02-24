import json
from document_loader import load_document
from llm_clients import call_chatgpt, call_gemini, call_claude
from compare_engine import compare_json, drift_score
from autocorrect_engine import autocorrect_json


def run_pipeline(path):

    print("\n=== Loading Document ===")
    text = load_document(path)

    print("\n=== Calling LLMs ===")
    outputs = {
        "chatgpt": call_chatgpt(text),
        "gemini": call_gemini(text),
        "claude": call_claude(text)
    }

    print("\n=== Raw Outputs ===")
    print(json.dumps(outputs, indent=4))

    print("\n=== Comparing JSON ===")
    comparisons = {
        "chatgpt_vs_gemini": compare_json(outputs["chatgpt"], outputs["gemini"]),
        "chatgpt_vs_claude": compare_json(outputs["chatgpt"], outputs["claude"]),
        "gemini_vs_claude": compare_json(outputs["gemini"], outputs["claude"]),
    }

    print(json.dumps(comparisons, indent=4))

    print("\n=== Calculating Drift Score ===")
    score = drift_score(comparisons)
    print("Drift Score:", score)

    print("\n=== Auto-Correcting Outputs ===")
    corrected = {
        model: autocorrect_json(output)
        for model, output in outputs.items()
    }

    print(json.dumps(corrected, indent=4))

    return {
        "outputs": outputs,
        "comparisons": comparisons,
        "drift_score": score,
        "corrected": corrected
    }


if __name__ == "__main__":
    result = run_pipeline("sample.pdf")
