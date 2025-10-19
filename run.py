import os
import sys
import subprocess
from pathlib import Path

def main():
    print("=" * 50)
    print("Simple Mistral AI FastAPI Demo")
    print("=" * 50)
    print()
    
    env_file = Path(".env")
    if not env_file.exists():
        print("Creating .env file from template...")
        env_example = Path("env.example")
        if env_example.exists():
            env_file.write_text(env_example.read_text())
            print("OK: Created .env file")
        else:
            print("ERROR: env.example file not found")
            return
    
    env_content = env_file.read_text()
    if "MISTRAL_API_KEY=your_mistral_api_key_here" in env_content:
        print("WARNING: Please set your MISTRAL_API_KEY in the .env file")
        print("   Get your API key from: https://console.mistral.ai/")
        return
    
    print("Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("OK: Dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to install dependencies: {e}")
        return
    
    print("\nStarting FastAPI server...")
    print("   Server: http://localhost:8000")
    print("   Docs: http://localhost:8000/docs")
    print("   Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app.main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\nServer stopped. Goodbye!")

if __name__ == "__main__":
    main()