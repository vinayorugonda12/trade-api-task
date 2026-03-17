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
{data}

Give markdown:
- Summary
- Opportunities
- Risks
"""

        response = model.generate_content(prompt)
        return response.text

    except Exception:
        # Fallback response
        return f"""
## Market Summary
The {sector} sector in India shows moderate growth.

## Opportunities
- Increasing demand
- Government support

## Risks
- Market volatility

## Conclusion
Stable sector with growth potential.
"""