# Name: Youssef Shafeek
# Date: 05/30/2025
# File Description: Main script to run the customer feedback analysis pipeline using LangGraph.
# It takes user input to filter and process data, runs the multi-agent system, evaluates the results,
# and exports a final document with insights and performance metrics.

from agents.workflow_graph import app
from utils.load_data import load_feedback_data
from evaluate_performance import evaluate_sentiment, evaluate_summary
from utils.export_pdf import export_to_pdf
from agents.document_agent import generate_document

# Load dataset
df = load_feedback_data("data/New_Feedback_Dataset_1000.csv")

# Allow the user to select the category and number of rows to analyze
category_input = input("Enter feedback category (Customer Support, Delivery, Pricing, Product Quality, or 'all'): ").strip()
num_rows_input = input("Enter number of rows to use (or type 'all'): ").strip()

# Filter by category
if category_input.lower() == "all":
    filtered_df = df
    category = "All Categories"
else:
    filtered_df = df[df["feedback_category"].str.lower() == category_input.lower()]
    category = category_input

# Handle row count
if num_rows_input.lower() == "all":
    selected_rows = filtered_df
else:
    num_rows = int(num_rows_input)
    selected_rows = filtered_df.head(num_rows)

# Prepare input data
feedback_list = selected_rows["feedback_text"].tolist()
raw_rows = selected_rows.to_dict(orient="records")
true_labels = [label.lower().strip() for label in selected_rows["sentiment"].tolist()]

# Run LangGraph pipeline
result = app.invoke({
    "original_feedback": feedback_list,
    "raw_feedback": raw_rows,
    "category": category
})

# --- Evaluation ---
# Parse sentiment summary string into individual labels for comparison
predicted_sentiments_raw = result["sentiment"].split("\n")
predicted_labels = []
for line in predicted_sentiments_raw:
    if ":" in line:
        label = line.split(":")[0].strip().lower()
        count = int(line.split(":")[1].split("(")[0].strip())
        predicted_labels.extend([label] * count)

# Evaluate and get text summaries
sentiment_report = evaluate_sentiment(true_labels=true_labels, predicted_labels=predicted_labels)
rouge_scores = evaluate_summary(reference_summary=feedback_list, generated_summary=result["processed_feedback"])

# Format ROUGE scores as a string for the document
rouge_text = "\n".join([
    f"{metric.upper()} - P: {score.precision:.2f}, R: {score.recall:.2f}, F1: {score.fmeasure:.2f}"
    for metric, score in rouge_scores.items()
])

# Generate final document using all enriched fields
final_document = generate_document(
    category=category,
    summary=result["summary"],
    insights=result["insights"],
    sentiment_label=result["sentiment"],
    original_feedback=feedback_list[0],
    processed_feedback=result["processed_feedback"][0],
    operational_performance=result.get("operational_performance", "N/A"),
    performance_metrics=sentiment_report,
    rouge_scores=rouge_text
)

# Output final result
print("\n=== Final Document with Evaluation ===")
print(final_document)

# Export final PDF
export_to_pdf(final_document, filename="customer_feedback_report.pdf")
