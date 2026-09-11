"""External API integration endpoints"""

import httpx
import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Any, Dict
from src.config.settings import settings
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger("ai_system")
router = APIRouter()


class ExternalAPIRequest(BaseModel):
    """External API request schema"""
    endpoint: str
    method: str = "GET"
    data: Optional[Dict[str, Any]] = None
    headers: Optional[Dict[str, str]] = None


@retry(stop=stop_after_attempt(settings.EXTERNAL_API_RETRY_ATTEMPTS),
        wait=wait_exponential(multiplier=1, min=2, max=10))
async def call_external_api(endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Dict:
    """Call external API with retry logic"""
    url = f"{settings.EXTERNAL_API_BASE_URL}{endpoint}"
    
    async with httpx.AsyncClient(timeout=settings.EXTERNAL_API_TIMEOUT) as client:
        try:
            if method == "GET":
                response = await client.get(url)
            elif method == "POST":
                response = await client.post(url, json=data)
            elif method == "PUT":
                response = await client.put(url, json=data)
            elif method == "DELETE":
                response = await client.delete(url)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            logger.error(f"External API error: {e}")
            raise


@router.get("/endpoints")
async def list_external_endpoints():
    """List available external API endpoints"""
    try:
        response = await call_external_api("/endpoints/ai/")
        return {
            "status": "success",
            "endpoints": response,
            "base_url": settings.EXTERNAL_API_BASE_URL
        }
    except Exception as e:
        logger.error(f"Failed to fetch endpoints: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch external endpoints")


@router.post("/call")
async def call_external_endpoint(request: ExternalAPIRequest):
    """Call external API endpoint"""
    try:
        response = await call_external_api(
            endpoint=request.endpoint,
            method=request.method,
            data=request.data
        )
        return {
            "status": "success",
            "data": response,
            "endpoint": request.endpoint
        }
    except Exception as e:
        logger.error(f"External API call failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models")
async def get_external_models():
    """Get available models from external API"""
    try:
        response = await call_external_api("/endpoints/ai/models")
        return {
            "status": "success",
            "models": response
        }
    except Exception as e:
        logger.error(f"Failed to fetch models: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch external models")


@router.post("/process")
async def process_with_external_api(request: ExternalAPIRequest):
    """Process request using external API"""
    try:
        response = await call_external_api(
            endpoint=request.endpoint,
            method=request.method,
            data=request.data
        )
        return {
            "status": "processed",
            "result": response
        }
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
