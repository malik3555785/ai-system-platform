"""
Model Management Endpoints
"""

import logging
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field

logger = logging.getLogger("ai_system")
router = APIRouter()


class ModelInfo(BaseModel):
    """Model information"""
    id: str
    name: str
    version: str
    provider: str
    capabilities: List[str]
    max_tokens: int
    cost_per_1k_input: float
    cost_per_1k_output: float
    status: str = "available"


# Available models
AVAILABLE_MODELS = [
    ModelInfo(
        id="gpt-5",
        name="GPT-5",
        version="5.0",
        provider="OpenAI",
        capabilities=["text-generation", "code-generation", "reasoning"],
        max_tokens=8192,
        cost_per_1k_input=0.03,
        cost_per_1k_output=0.06,
    ),
    ModelInfo(
        id="gpt-5-mini",
        name="GPT-5 Mini",
        version="5.0",
        provider="OpenAI",
        capabilities=["text-generation", "code-generation"],
        max_tokens=4096,
        cost_per_1k_input=0.01,
        cost_per_1k_output=0.02,
    ),
    ModelInfo(
        id="claude-opus",
        name="Claude Opus 4.8",
        version="4.8",
        provider="Anthropic",
        capabilities=["text-generation", "reasoning", "analysis"],
        max_tokens=100000,
        cost_per_1k_input=0.015,
        cost_per_1k_output=0.075,
    ),
    ModelInfo(
        id="claude-sonnet",
        name="Claude Sonnet 4.6",
        version="4.6",
        provider="Anthropic",
        capabilities=["text-generation", "code-generation"],
        max_tokens=200000,
        cost_per_1k_input=0.003,
        cost_per_1k_output=0.015,
    ),
]


@router.get("/", response_model=List[ModelInfo])
async def list_models():
    """
    List all available models
    """
    return AVAILABLE_MODELS


@router.get("/{model_id}", response_model=ModelInfo)
async def get_model(model_id: str):
    """
    Get specific model information
    """
    for model in AVAILABLE_MODELS:
        if model.id == model_id:
            return model
    return {"error": f"Model {model_id} not found"}
