from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import Response
from app.services.data_service import fetch_market_data
from app.services.ai_service import analyze_data
from app.utils.auth import verify_api_key
from app.utils.session import track_session
from app.utils.rate_limiter import limiter

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str, api_key=Depends(verify_api_key)):

    # validation 
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector name")

    ip = request.client.host
    session = track_session(ip)

    data = fetch_market_data(sector)
    report = analyze_data(sector, data)

    return Response(
        content=report,
        media_type="text/markdown",
        headers={
            "Content-Disposition": f"attachment; filename={sector}_report.md"
        }
    )