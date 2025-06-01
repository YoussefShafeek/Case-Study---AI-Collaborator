# Name: Youssef Shafeek
# Date: 05/28/2025
# File Description: This module creates a documentation agent that generates a structured
# document report based on the processed customer feedback. It combines the ouputs from the other agents 
# (sentiment, summary, operational performance evaluation, insights) into a readable document. 
# This document is used for reporting and is exported into a pdf

# Utilized to include the current date in the document
from datetime import datetime

# This function assembles all processed feedback analysis into a structured and readable
# document. The generated document is returned as a formatted string that can be printed or exported.
def generate_document(
    category: str,
    summary: str,
    insights: str,
    sentiment_label: str = None,
    original_feedback: str = None,
    processed_feedback: str = None,
    operational_performance: str = None,
    performance_metrics: str = None, 
    rouge_scores: str = None          
) -> str:
    # Get the current date
    today = datetime.today().strftime("%B %d, %Y")

    doc = f"""
==============================
Customer Feedback Analysis Report
==============================

Date: {today}
Feedback Category: {category}

------------------------------
Processed Feedback Sample
------------------------------
Original: {original_feedback}
Processed: {processed_feedback}

------------------------------
Sentiment Classification
------------------------------
Predicted Sentiment: 
{sentiment_label}

------------------------------
Summarized Feedback Themes
------------------------------
{summary}

------------------------------
Actionable Insights
------------------------------
{insights}

------------------------------
Operational Performance Summary
------------------------------
{operational_performance}

------------------------------
Performance Evaluation
------------------------------
Classification Metrics:
{performance_metrics}

Summarization Quality (ROUGE):
{rouge_scores}
""".strip() # This removes any whitespace for clean output
    # Return the final document
    return doc
