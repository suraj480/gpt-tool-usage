from llm_client import ask

def risky_action(action_description):
    """Pretend this sends a real email, charges a card, deletes a file, etc."""
    print(f"EXECUTED: {action_description}")

def request_human_approval(action_description):
    """The approval gate: pause and ask a human before proceeding."""
    print(f"\n>>> APPROVAL NEEDED <<<")
    print(f"Proposed action: {action_description}")
    response = input("Approve this action? (y/n): ")
    return response.strip().lower() == "y"

#Step 1: the agent proposes an action
user_request = "Refund the customer $500 for their damaged order."

proposed_action = ask(
    "You are a support agent. Based on the request, state the EXACT "
    "action you want to take in one sentence.",
    user_request
)
print("Agent proposes:", proposed_action)

# Step 2: approval gate BEFORE the action runs
HIGH_RISK_KEYWORDS = ["refund", "delete", "cancel", "charge"]
is_high_risk = any(word in proposed_action.lower() for word in HIGH_RISK_KEYWORDS)

if is_high_risk:
    approved = request_human_approval(proposed_action)
    if approved:
        risky_action(proposed_action)
    else:
        print("Action REJECTED by human. Agent must find an alternative or stop.")
        # Feedback injection: tell the agent WHY, so it can adjust
        alternative = ask(
            "Your proposed action was rejected by a human reviewer. "
            "Suggest a safer alternative next step.",
            f"Rejected action: {proposed_action}"
        )
        print("Agent's alternative:", alternative)
else:
    print("Low-risk action, proceeding without approval.")
    risky_action(proposed_action)