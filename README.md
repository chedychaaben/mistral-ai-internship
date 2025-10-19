# Simple Mistral AI FastAPI Demo

A simple FastAPI application showcasing Mistral AI capabilities for an internship test.

## Features

- **Text Generation**: Generate text using Mistral AI
- **Code Generation**: Generate code in various languages
- **Text Summarization**: Summarize long texts
- **Sentiment Analysis**: Analyze text sentiment
- **Translation**: Translate text between languages

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**
   ```bash
   cp env.example .env
   # Edit .env and add your Mistral API key
   ```

3. **Run the application**
   ```bash
   python run.py
   # or
   uvicorn app.main:app --reload
   ```

4. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## API Endpoints

- `POST /generate-text` - Generate text
- `POST /generate-code` - Generate code
- `POST /summarize` - Summarize text
- `POST /analyze-sentiment` - Analyze sentiment
- `POST /translate` - Translate text

## Environment Variables

- `MISTRAL_API_KEY` - Your Mistral AI API key (required)

## Example Usage

```bash
# Generate text
curl -X POST "http://localhost:8000/generate-text" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Write a short story about a robot", "max_tokens": 200}'

# Generate code
curl -X POST "http://localhost:8000/generate-code" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Create a Python function to sort a list", "language": "python"}'

# Summarize text
curl -X POST "http://localhost:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{"text": "Your long text here...", "max_length": 100}'
```

## Project Structure

```
mistral-ai-internship/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   └── services/
│       └── mistral_service.py # Mistral AI integration
├── requirements.txt         # Dependencies
├── env.example             # Environment template
├── run.py                  # Quick start script
└── README.md               # This file
```
