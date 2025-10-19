# Mistral AI FastAPI Demo

A simple FastAPI application that integrates with Mistral AI for text generation, code generation, and analysis.

## Features

- Text generation using Mistral AI
- Code generation in multiple languages
- Text summarization
- Sentiment analysis
- Language translation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment:
   ```bash
   cp env.example .env
   # Add your Mistral API key to .env
   ```

3. Run the application:
   ```bash
   python run.py
   ```

## API Endpoints

- `POST /generate-text` - Generate text
- `POST /generate-code` - Generate code
- `POST /summarize` - Summarize text
- `POST /analyze-sentiment` - Analyze sentiment
- `POST /translate` - Translate text

## Usage Examples

```bash
# Generate text
curl -X POST "http://localhost:8000/generate-text" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Write a story about AI", "max_tokens": 200}'

# Generate code
curl -X POST "http://localhost:8000/generate-code" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Create a sorting function", "language": "python"}'
```

## Project Structure

```
├── app/
│   ├── main.py
│   ├── models/schemas.py
│   └── services/mistral_service.py
├── requirements.txt
├── env.example
└── run.py
```
