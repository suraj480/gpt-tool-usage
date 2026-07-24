import pandas as pd


APPROVAL_THRESHOLD = 10000

SUSPICIOUS_MEMO_PHRASES = [
    "urgent",
    "per phone instructions",
    "wire immediately",
    "confidential"
]


def flag_risk_signals(row, all_rows):
    """
    Explainable risk checks.
    Returns a list of risk signals.
    """

    signals = []

    # Risk Signal 1: Very large transaction
    if row["amount"] > 100000:
        signals.append(
            f"very large amount (${row['amount']:,})"
        )

    # Risk Signal 2: Suspicious memo language
    memo_lower = str(row["memo"]).lower()

    for phrase in SUSPICIOUS_MEMO_PHRASES:
        if phrase in memo_lower:
            signals.append(
                f"memo contains suspicious phrase: '{phrase}'"
            )

    # Risk Signal 3: Unknown recipient
    if "unknown" in str(row["recipient_name"]).lower():
        signals.append(
            "recipient name suggests an unverified/unfamiliar party"
        )

    # Risk Signal 4 (Homework): New payee detection
    previous_recipients = set(
        all_rows[
            all_rows["transfer_id"] != row["transfer_id"]
        ]["recipient_name"]
    )

    if row["recipient_name"] not in previous_recipients:
        signals.append(
            "recipient is a new payee not seen in previous transfers"
        )

    return signals


def create_summary(row, signals):
    """
    Creates the human review screen.
    """

    summary = f"""
Transfer {row['transfer_id']} exceeds the ${APPROVAL_THRESHOLD:,} approval threshold — PAUSING for human review.

Transfer ID:  {row['transfer_id']}
From:         {row['sender_name']}
To:           {row['recipient_name']}
Amount:       ${row['amount']:,} USD
Memo:         {row['memo']}
"""

    if signals:
        summary += "\n⚠️  RISK SIGNALS FLAGGED:\n"
        for signal in signals:
            summary += f"- {signal}\n"
    else:
        summary += "\nNo automatic risk signals flagged.\n"

    return summary


def get_human_decision(summary_text):

    print(summary_text)

    decision = input(
        "\nApprove, Reject, or Modify this transfer? [a/r/m]: "
    )

    return decision


def process_decision(decision, row):

    decision = decision.strip().lower()

    if decision == "a":
        return (
            f"✅ APPROVED — transfer "
            f"{row['transfer_id']} would now be executed."
        )

    elif decision == "r":
        return (
            f"❌ REJECTED — transfer "
            f"{row['transfer_id']} cancelled, sender notified."
        )

    elif decision == "m":
        return (
            f"✏️ MODIFICATION REQUESTED — transfer "
            f"{row['transfer_id']} routed back to preparer."
        )

    else:
        # Fail closed
        return (
            f"⚠️ INVALID INPUT ('{decision}') — "
            f"defaulting to REJECTED for safety."
        )


def main():

    df = pd.read_csv("data/transfer_requests.csv")

    for _, row in df.iterrows():

        if row["amount"] > APPROVAL_THRESHOLD:

            signals = flag_risk_signals(row, df)

            summary = create_summary(
                row,
                signals
            )

            decision = get_human_decision(summary)

            result = process_decision(
                decision,
                row
            )

            print(result)

        else:

            print(
                f"\nTransfer {row['transfer_id']} "
                f"(${row['amount']:,}) is below the approval threshold."
            )

            print(
                f"✅ Transfer {row['transfer_id']} "
                "executed automatically."
            )


if __name__ == "__main__":
    main()