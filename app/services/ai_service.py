import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_data(sector: str, data: str):
    try:
        model = genai.GenerativeModel("models/gemini-flash-latest")

        prompt = f"""
Analyze the {sector} sector in India.

Data:
{data[:200]}

Provide a structured markdown report:

## Market Summary
## Key Trends
## Trade Opportunities
## Risks
## Conclusion
"""

        response = model.generate_content(prompt)

        return response.text if response.text else "No response from AI"

    except Exception as e:
        # ✅ ADD THIS HERE
        print("Gemini Error:", e)

        return f"Error: {str(e)}"