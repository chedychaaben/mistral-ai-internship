"""
Simple Pydantic schemas for the API
"""

from pydantic import BaseModel, Field
from typing import Optional


class TextGenerationRequest(BaseModel):
    """Request schema for text generation"""
    prompt: str = Field(..., description="The text prompt")
    max_tokens: int = Field(500, description="Maximum tokens to generate")
    temperature: float = Field(0.7, description="Sampling temperature")


class CodeGenerationRequest(BaseModel):
    """Request schema for code generation"""
    prompt: str = Field(..., description="Code generation prompt")
    language: str = Field("python", description="Programming language")
    max_tokens: int = Field(1000, description="Maximum tokens to generate")
