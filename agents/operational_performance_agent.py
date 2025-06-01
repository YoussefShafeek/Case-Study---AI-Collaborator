# Name: Youssef Shafeek
# Date: 05/29/2025
# File Description: This module evaluayes operational performance bas on the feedback data
# It calculates how effectively feedback marked as response required was resolved and
# generates a short summary with a resolution rate

from typing import List

# This function calculates the resolution rate for customer feedback that required a response. 
# Depends on the rate, it will generate a small summary for the performance
def analyze_operational_performance(rows: List[dict]) -> str:
    # Total number of rows being analyzed
    total = len(rows)
    # Count how many rows needed a response
    required = sum(1 for r in rows if str(r["response_required"]).strip().lower() == "yes")
    # count how many of those responses were resolved
    resolved = sum(1 for r in rows if str(r["response_required"]).strip().lower() == "yes"
                   and str(r["resolved"]).strip().lower() == "yes")

    # Calculate the resolution rate 
    # handles case where divide by 0 happens
    resolution_rate = resolved / required if required > 0 else 1.0

    # Generate a summary depending on the rate
    if resolution_rate == 1.0:
        summary = "All required feedback responses have been resolved, showing excellent operational responsiveness."
    elif resolution_rate >= 0.75:
        summary = "Most required feedback responses have been resolved, indicating strong responsiveness."
    elif resolution_rate >= 0.4:
        summary = "Some feedback was resolved, but responsiveness can be improved."
    else:
        summary = "Operational response rate is low, with many unresolved feedback items."

    # Return summary with rate as a percentage
    return f"{summary} Resolution rate: {resolution_rate:.0%} of required responses."
