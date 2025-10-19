"""
Simple test to verify the application works
"""

import requests
import json

def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:8000"
    
    print("Testing Mistral AI FastAPI Demo...")
    print("=" * 40)
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check: OK")
        else:
            print("❌ Health check: FAILED")
    except:
        print("❌ Health check: Server not running")
        return
    
    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Root endpoint: OK")
        else:
            print("❌ Root endpoint: FAILED")
    except:
        print("❌ Root endpoint: FAILED")
    
    print("\nAPI is running! Visit http://localhost:8000/docs for full documentation")

if __name__ == "__main__":
    test_api()
