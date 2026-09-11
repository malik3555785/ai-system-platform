"""Model management endpoints"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Model(BaseModel):
    """Model schema"""
    name: str
    provider: str
    version: str
    description: str
    enabled: bool = True


AVAILABLE_MODELS = [
    Model(name="gpt-4", provider="OpenAI", version="4.0", description="GPT-4 Model"),
    Model(name="gpt-3.5-turbo", provider="OpenAI", version="3.5", description="GPT-3.5 Turbo"),
    Model(name="claude-3", provider="Anthropic", version="3.0", description="Claude 3 Model"),
    Model(name="claude-2", provider="Anthropic", version="2.0", description="Claude 2 Model"),
]


@router.get("/list")
async def list_models():
    """List all available models"""
    return {"models": AVAILABLE_MODELS, "count": len(AVAILABLE_MODELS)}


@router.get("/{model_name}")
async def get_model(model_name: str):
    """Get specific model details"""
    for model in AVAILABLE_MODELS:
        if model.name == model_name:
            return model
    raise HTTPException(status_code=404, detail="Model not found")


@router.post("/initialize")
async def initialize_model(model_name: str):
    """Initialize a model"""
    for model in AVAILABLE_MODELS:
        if model.name == model_name:
            return {"status": "initialized", "model": model}
    raise HTTPException(status_code=404, detail="Model not found")
