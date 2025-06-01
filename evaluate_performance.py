# Name: Youssef Shafeek
# Date: 05/30/2025
# File Description: This module conducts an evaluation of the multi agent system built.
# It measures the performance of the sentiment agent using accuracy. Uses ROUGE metrics
# to evaluate the quality of the summary. Results are printed and documented 

from sklearn.metrics import classification_report, accuracy_score
from rouge_score import rouge_scorer
from typing import List

# This function evaluates the performance of the sentiment agent.
def evaluate_sentiment(true_labels, predicted_labels):
    # Classification metrics like precision, recall and F1-scores from sklearn
    report = classification_report(true_labels, predicted_labels, zero_division=0)
    # Compute accuracy score by comparing true labels to predicted labels
    accuracy = accuracy_score(true_labels, predicted_labels)
    # Print report
    print("\n=== Sentiment Classification Report ===")
    print(report)
    print(f"Accuracy: {accuracy:.2f}")
    return report

# This function computes the ROUGE metrics to assess the quality of the generated summary 
def evaluate_summary(reference_summary: list[str], generated_summary: list[str]):
    # Initialize with common Rouge metrics (ROUGE 1, ROUGE 2, ROUGE 3)
    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL"], use_stemmer=True)
    
    # Join the lists into single strings
    reference_text = " ".join(reference_summary)
    generated_text = " ".join(generated_summary)

    # Calculate the scores
    scores = scorer.score(reference_text, generated_text)

    # Print the ROUGE scores
    print("\n=== ROUGE Scores ===")
    for metric, result in scores.items():
        print(f"{metric.upper()} - Precision: {result.precision:.2f}, Recall: {result.recall:.2f}, F1: {result.fmeasure:.2f}")

    return scores

