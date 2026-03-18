from fastapi import FastAPI
from app.routes.analyze import router
from app.utils.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Trade Opportunities API is running 🚀"}

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)

from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"message": "Rate limit exceeded"}
    )
