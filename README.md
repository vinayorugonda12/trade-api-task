# trade-api-task
FastAPI-based Trade Opportunities API that uses Gemini AI to generate real-time market analysis reports with authentication, rate limiting, and markdown output.
# Trade Opportunities API

## Overview

The Trade Opportunities API is a FastAPI-based backend service that analyzes market data and generates AI-powered trade insights for different sectors in India.

It leverages Google's Gemini LLM to provide structured, real-time market analysis in **markdown format**, helping users identify opportunities, trends, and risks.

---

##  Tech Stack

* **Backend:** FastAPI
* **AI Model:** Google Gemini API
* **Data Source:** DuckDuckGo (web search)
* **Rate Limiting:** SlowAPI
* **Authentication:** API Key
* **Storage:** In-memory (session tracking)

---

## Features

* 📊 Sector-based market analysis (e.g., pharma, tech, agriculture)
* 🤖 AI-powered insights using Gemini
* 🔐 API Key authentication
* ⏱️ Rate limiting (5 requests/min)
* 🧠 Session tracking per user (IP-based)
* 📄 Markdown report generation
* 📥 Downloadable `.md` reports
* ⚠️ Graceful error handling with fallback responses
* 🧾 Logging for monitoring and debugging

---

## 📡 API Endpoint

### 🔹 Analyze Sector

```http
GET /analyze/{sector}
```

### 🔹 Example

```http
GET /analyze/pharmaceuticals
```

### 🔹 Headers

```http
x-api-key: mysecretkey
```

---

## 📥 Response

Returns a **markdown report** with:

* Market Summary
* Key Trends
* Trade Opportunities
* Risks
* Conclusion

Example:

```markdown
## Market Summary
The Indian pharmaceutical sector is growing rapidly...

## Opportunities
- Export growth
- Domestic demand

## Risks
- Regulatory challenges
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/trade-api.git
cd trade-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Server

```bash
python -m uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Swagger UI available at:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Security

* API Key authentication
* Input validation
* Rate limiting per IP
* Error handling for external API failures

---

## 🧠 Architecture

The project follows a clean modular structure:

```
app/
 ├── routes/        # API endpoints
 ├── services/      # Business logic (AI + data)
 ├── utils/         # Auth, rate limit, session
 ├── models/        # Request validation
```

---

## ⚠️ Limitations

* Uses free-tier Gemini API (quota limits may apply)
* Data source is basic (can be enhanced with real APIs)

---

 Frontend dashboard (React)

---

## 👨‍💻 Author

Vinay Orugonda

---

## ⭐ Acknowledgment

Built as part of a backend developer assignment to demonstrate API design, AI integration, and scalable architecture.
