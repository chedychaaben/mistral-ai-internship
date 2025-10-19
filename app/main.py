"""
Simple Mistral AI FastAPI Demo

A simple FastAPI application showcasing Mistral AI capabilities
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv

from app.services.mistral_service import mistral_service
from app.models.schemas import TextGenerationRequest, CodeGenerationRequest

# Load environment variables
load_dotenv()

# Create FastAPI application
app = FastAPI(
    title="Mistral AI Demo",
    description="Simple demo of Mistral AI capabilities",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Mistral AI Demo API",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "API is running"}

@app.post("/generate-text")
async def generate_text(request: TextGenerationRequest):
    """Generate text using Mistral AI"""
    try:
        generated_text = await mistral_service.generate_text(
            prompt=request.prompt,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        return {"generated_text": generated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-code")
async def generate_code(request: CodeGenerationRequest):
    """Generate code using Mistral AI"""
    try:
        generated_code = await mistral_service.generate_code(
            prompt=request.prompt,
            language=request.language,
            max_tokens=request.max_tokens
        )
        return {"generated_code": generated_code, "language": request.language}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def summarize_text(text: str, max_length: int = 200):
    """Summarize text using Mistral AI"""
    try:
        summary = await mistral_service.summarize_text(text, max_length)
        return {"summary": summary, "original_length": len(text.split())}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-sentiment")
async def analyze_sentiment(text: str):
    """Analyze sentiment using Mistral AI"""
    try:
        result = await mistral_service.analyze_sentiment(text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/translate")
async def translate_text(text: str, target_language: str = "Spanish"):
    """Translate text using Mistral AI"""
    try:
        translated = await mistral_service.translate_text(text, target_language)
        return {"translated_text": translated, "target_language": target_language}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
