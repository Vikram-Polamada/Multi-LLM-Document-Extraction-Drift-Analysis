import json

EXPECTED_SCHEMA = {
    "title": str,
    "author": str,
    "date": str,
    "key_points": list,
    "summary": str
}

def autocorrect_json(data):
    corrected = {}

    for field, dtype in EXPECTED_SCHEMA.items():

        if field not in data:
            corrected[field] = [] if dtype == list else "UNKNOWN"
            continue

        value = data[field]

        # Correct lists
        if dtype == list:
            if not isinstance(value, list):
                corrected[field] = [str(value)]
            else:
                corrected[field] = [str(v) for v in value]
            continue

        # Correct strings
        corrected[field] = str(value)

    return corrected
