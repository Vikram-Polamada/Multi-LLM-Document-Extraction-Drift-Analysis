def compare_json(a, b):
    diffs = {}
    keys = set(a.keys()).union(b.keys())

    for k in keys:
        if a.get(k) != b.get(k):
            diffs[k] = (a.get(k), b.get(k))

    return diffs


def drift_score(diffs_dict):
    issues = sum(len(v) for v in diffs_dict.values())
    return max(0, 100 - issues * 5)
