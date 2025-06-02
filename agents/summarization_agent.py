# Name: Youssef Shafeek
# Date: 05/27/2025
# File Description: This module defines the summarization agent. It uses GPT based LLM
# to generate a concise objective summary the key themes expressed in the customer feedback

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variable (OpenAI API key from .env file)
load_dotenv()

# Intitialize the language model with a deterministic output (temperature = 0)
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

# Prompt to produce a summary based on multiple feedbacks
prompt = ChatPromptTemplate.from_template("""
You are an expert summarizer.

Given the following list of customer feedback entries, generate a concise paragraph summarizing the key themes, concerns or positive comments.
                                        
Be professional, objective, and clear.

Customer Feedback:
{feedback_list}

Summary:
""")

# Combine prompt and model
summary_chain = prompt | llm

# Function to call the paragraph summarizing the common themes in a list of customer feedback
def summarize_feedback(feedback_texts: list[str]) -> str:
    # Join the list into a single string
    joined_feedback = "\n- " + "\n- ".join(feedback_texts)
    result = summary_chain.invoke({"feedback_list": joined_feedback})
    return result.content.strip()
