# Name: Youssef Shafeek
# Date: 05/27/2025
# File Description: This module defines the NLP processing agent responsible for cleaning
# messy customer feedback. It uses GPT based LLM to produce gramatically correct
# and readable sentences while trying preserving the original content

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variable (OpenAI API key from .env file)
load_dotenv()

# Intitialize the language model with a deterministic output (temperature = 0)
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# Define the prompt template to guide the LLM to turn messy feedback to clean and correct feedback
prompt = ChatPromptTemplate.from_template("""
You are an assistant that rewrites messy or fragmented customer feedback into clean, grammatically correct sentences. 
However, your top priority is to preserve the original emotional tone, urgency, and intent.

Instructions:
- Retain all emotional expressions (e.g., "frustrated", "love", "terrible", "very slow").
- Do not soften or neutralize tone.
- Fix grammar, punctuation, or broken structure only when needed.
- If the original text is already clear, return it unchanged.

Original Feedback:
{feedback}

Cleaned Feedback:
""")

# Creates a runnable LLM chain that combines the model and prompt
rewrite_chain = prompt | llm

# Function takes in raw customer feedback and returns grammatically correct version
# using GPT based LLM
def process_feedback(feedback_text: str) -> str:
    # Invoke the LLM with the formatted list
    result = rewrite_chain.invoke({"feedback": feedback_text})
    # Return only the content portion, removing any whitespace
    return result.content.strip()
