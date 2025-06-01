# Name: Youssef Shafeek
# Date: 05/29/2025
# File Description: This module defines the architecture of the multi-agent system using LangGraph.
# It chains together GPT based agents for processing,
# analyzing, summarizing and documenting customer feedback. The output is a
# structured report with insights, sentiment classification, performance metrics,
# and operational response analysis.

from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from typing import TypedDict
from collections import Counter

# Import agents from their modules
from agents.nlp_processing_agent import process_feedback
from agents.sentiment_agent import get_sentiment
from agents.summarization_agent import summarize_feedback
from agents.insights_agent import generate_insights
from agents.document_agent import generate_document
from agents.operational_performance_agent import analyze_operational_performance  

# Define the shared state structure that all agents will read or write to 
class FeedbackState(TypedDict):
    original_feedback: list[str]
    processed_feedback: list[str]
    sentiment: str
    summary: str
    insights: str
    document: str
    category: str
    raw_feedback: list[dict]  
    operational_performance: str  
    performance_metrics: str  
    rouge_scores: str         

# nlp_processing_agent
nlp_node = RunnableLambda(lambda state: {
    "processed_feedback": [process_feedback(text) for text in state["original_feedback"]]
})

# sentiment_agent
def get_sentiment_summary(feedback_list: list[str]) -> str:
    sentiments = [get_sentiment(text) for text in feedback_list]
    counts = Counter(sentiments)
    total = sum(counts.values())
    return "\n".join([
        f"{label}: {count} ({(count / total * 100):.0f}%)"
        for label, count in counts.items()
    ])

sentiment_node = RunnableLambda(lambda state: {
    "sentiment": get_sentiment_summary(state["processed_feedback"])
})

# summarization_agent
summarization_node = RunnableLambda(lambda state: {
    "summary": summarize_feedback(state["processed_feedback"])
})

# insights_agent
insights_node = RunnableLambda(lambda state: {
    "insights": generate_insights(state["processed_feedback"])
})

# operational_performance_agent
operational_node = RunnableLambda(lambda state: {
    "operational_performance": analyze_operational_performance(state["raw_feedback"])
})

# document_agent
document_node = RunnableLambda(lambda state: {
    "document": generate_document(
        category=state.get("category", "Unknown"),
        summary=state["summary"],
        insights=state["insights"],
        sentiment_label=state["sentiment"],
        original_feedback=state["original_feedback"][0],
        processed_feedback=state["processed_feedback"][0],
        operational_performance=state.get("operational_performance", "N/A"),
        performance_metrics=state.get("performance_metrics", "N/A"),
        rouge_scores=state.get("rouge_scores", "N/A")
    )
})

# Build LangGraph workflow by connecting each agent node in sequence
graph = StateGraph(FeedbackState)
graph.add_node("NLPProcessingAgent", nlp_node)
graph.add_node("SentimentAgent", sentiment_node)
graph.add_node("SummarizationAgent", summarization_node)
graph.add_node("InsightsAgent", insights_node)
graph.add_node("OperationalPerformanceAgent", operational_node)
graph.add_node("DocumentAgent", document_node)

# Define the execution order by adding edges
graph.set_entry_point("NLPProcessingAgent")
graph.add_edge("NLPProcessingAgent", "SentimentAgent")
graph.add_edge("SentimentAgent", "SummarizationAgent")
graph.add_edge("SummarizationAgent", "InsightsAgent")
graph.add_edge("InsightsAgent", "OperationalPerformanceAgent")
graph.add_edge("OperationalPerformanceAgent", "DocumentAgent")
graph.add_edge("DocumentAgent", END)

# Compile the graph 
app = graph.compile()
