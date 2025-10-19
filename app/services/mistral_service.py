"""
Simple Mistral AI service
"""

from mistralai import Mistral
from typing import Dict, Any
import json
import os

class MistralService:
    """Simple service for Mistral AI"""
    
    def __init__(self):
        """Initialize Mistral client"""
        api_key = os.getenv("MISTRAL_API_KEY")
        if not api_key or api_key == "your_mistral_api_key_here":
            print("WARNING: MISTRAL_API_KEY not set. Using demo mode.")
            self.client = None
            self.model = "mistral-large-latest"
            self.demo_mode = True
        else:
            self.client = Mistral(api_key=api_key)
            self.model = "mistral-large-latest"
            self.demo_mode = False
    
    async def generate_text(self, prompt: str, max_tokens: int = 500, temperature: float = 0.7) -> str:
        """Generate text using Mistral AI"""
        if self.demo_mode:
            return f"[DEMO] Generated text for prompt: '{prompt[:50]}...' (Set MISTRAL_API_KEY to use real AI)"
        
        try:
            messages = [{"role": "user", "content": prompt}]
            response = self.client.chat(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Text generation failed: {str(e)}")
    
    async def generate_code(self, prompt: str, language: str = "python", max_tokens: int = 1000) -> str:
        """Generate code using Mistral AI"""
        if self.demo_mode:
            return f"# [DEMO] {language} code for: {prompt[:50]}...\n# Set MISTRAL_API_KEY to use real AI\nprint('Hello, World!')"
        
        system_prompt = f"You are an expert {language} programmer. Generate clean, well-documented code. Only return the code."
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            response = self.client.chat(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Code generation failed: {str(e)}")
    
    async def summarize_text(self, text: str, max_length: int = 200) -> str:
        """Summarize text using Mistral AI"""
        if self.demo_mode:
            return f"[DEMO] Summary of text ({len(text.split())} words): {text[:100]}... (Set MISTRAL_API_KEY to use real AI)"
        
        system_prompt = f"Create a concise summary in approximately {max_length} words or less."
        prompt = f"Summarize this text:\n\n{text}"
        
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            response = self.client.chat(
                model=self.model,
                messages=messages,
                max_tokens=max_length * 2,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Summarization failed: {str(e)}")
    
    async def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment using Mistral AI"""
        if self.demo_mode:
            return {
                "sentiment": "neutral",
                "confidence": 0.5,
                "explanation": f"[DEMO] Sentiment analysis for: '{text[:50]}...' (Set MISTRAL_API_KEY to use real AI)"
            }
        
        system_prompt = """Analyze the sentiment and return JSON with:
        - sentiment: "positive", "negative", or "neutral"
        - confidence: number between 0 and 1
        - explanation: brief explanation"""
        
        prompt = f"Analyze sentiment: {text}"
        
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
            response = self.client.chat(
                model=self.model,
                messages=messages,
                max_tokens=200,
                temperature=0.3
            )
            
            result = response.choices[0].message.content
            try:
                return json.loads(result)
            except json.JSONDecodeError:
                return {
                    "sentiment": "neutral",
                    "confidence": 0.5,
                    "explanation": result
                }
        except Exception as e:
            raise Exception(f"Sentiment analysis failed: {str(e)}")
    
    async def translate_text(self, text: str, target_language: str = "Spanish") -> str:
        """Translate text using Mistral AI"""
        if self.demo_mode:
            return f"[DEMO] Translation to {target_language}: '{text}' (Set MISTRAL_API_KEY to use real AI)"
        
        system_prompt = f"Translate the text to {target_language}. Return only the translation."
        
        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ]
            response = self.client.chat(
                model=self.model,
                messages=messages,
                max_tokens=len(text) * 2,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")

# Global service instance
mistral_service = MistralService()
