# Case-Study---AI-Collaborator
Multi-Agent System for Chatbot and Document Creation Based on Customer Feedback

Description: This project is an AI-powered multi-agent system that automates the analysis of customer feedback using a LangGraph workflow. It processes unstructured feedback, performs sentiment classification, extracts insights, summarizes key themes and exports the results into a structured PDF report for business decision-makers.

How to run:
1) Clone repository:
   git clone https://github.com/YoussefShafeek/Case-Study---AI-Collaborator.git
   cd Case-Study---AI-Collaborator
  
2) Install dependencies:
   pip install -r requirements.txt
  
3) Add Your OpenAI API key to .env file:
   OPENAI_API_KEY=your-api-key

4) Run the main script:
   python main.py

Project Structure:
- 'main.py' – Entry point for running the full analysis
- 'agents/' – Contains all LangGraph agents (NLP, Sentiment, etc.)
- 'utils/' – Utility functions (PDF export, data loading)
- 'evaluate_performance.py' – Accuracy and ROUGE score evaluation
- `requirements.txt' – Python dependencies
