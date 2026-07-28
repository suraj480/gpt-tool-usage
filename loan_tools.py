POLICY_KB = {
    "POL001": "Low Risk",
    "POL002": "Medium Risk",
    "POL003": "High Risk"
}

def search_credit_policy(query, kb):
    if "late payment" in query.lower():
        return {
            "policy_id": "POL002",
            "policy": kb["POL002"]
        }

    return {
        "policy_id": "POL001",
        "policy": kb["POL001"]
    }