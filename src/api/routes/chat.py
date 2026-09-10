"""
Chat Completion Endpoints
"""

import logging
from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

logger = logging.getLogger("ai_system")
router = APIRouter()


class Message(BaseModel):
    """Chat message"""
    role: str = Field(..., description="Role: 'user', 'assistant', or 'system'")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    """Chat completion request"""
    model: str = Field("gpt-5", description="Model ID")
    messages: List[Message] = Field(..., description="Messages")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Temperature")
    max_tokens: int = Field(1000, ge=1, description="Max tokens")
    top_p: float = Field(1.0, ge=0.0, le=1.0, description="Top P")


class ChatResponse(BaseModel):
    """Chat completion response"""
    id: str
    model: str
    timestamp: str
    message: Message
    usage: dict
    stop_reason: str


@router.post("/completions", response_model=ChatResponse)
async def create_chat_completion(request: ChatRequest):
    """
    Create a chat completion
    """
    logger.info(f"Chat request: model={request.model}, messages={len(request.messages)}")
    
    # Mock response for demonstration
    return ChatResponse(
        id="chat-001",
        model=request.model,
        timestamp=datetime.utcnow().isoformat(),
        message=Message(
            role="assistant",
            content="This is a demonstration response. Connect to real models for actual responses."
        ),
        usage={
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30,
        },
        stop_reason="stop",
    )


@router.post("/stream")
async def stream_chat_completion(request: ChatRequest):
    """
    Stream a chat completion
    """
    logger.info(f"Stream request: model={request.model}")
    
    async def generate():
        chunks = [
            {"chunk": "This ", "index": 0},
            {"chunk": "is ", "index": 1},
            {"chunk": "a ", "index": 2},
            {"chunk": "streaming ", "index": 3},
            {"chunk": "response.", "index": 4},
        ]
        for chunk in chunks:
            yield f"data: {chunk}\n\n"
    
    return generate()
