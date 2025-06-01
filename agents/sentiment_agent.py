# Name: Youssef Shafeek
# Date: 05/27/2025
# File Description: This module defines the sentiment analysis agent. It uses a GPT
# LLM  to decide whether customer feedback is a Positive, Negative or Neutral sentiment

from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variable (OpenAI API key from .env file)
load_dotenv()

# Intitialize the language model with a deterministic output (temperature = 0)
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# Define prompt for the LLM to figure out the sentiment of customer feedback
prompt = ChatPromptTemplate.from_template("""
You are a sentiment analysis expert.

Classify the sentiment of the customer’s message as exactly one of these:
- Positive
- Negative
- Neutral

Guidelines:
- Use "Neutral" ONLY if the message contains no clear praise or dissatisfaction.
- If there are mixed emotions, choose the **dominant** one.
- Be concise. Output just one word: Positive, Neutral, or Negative.

                                          
Feedback:
{feedback}

Sentiment:
""")

# Combine prompt and model
sentiment_chain = prompt | llm

# Function classifies the sentiment of a single customer feedback
def get_sentiment(feedback_text: str) -> str:
    result = sentiment_chain.invoke({"feedback": feedback_text})
    return result.content.strip().lower()

