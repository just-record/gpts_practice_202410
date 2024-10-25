import requests
import json

# API base URL
### 실제 GPTs의 API로 사용 하기 위해서는 HTTPS여야 함 - HTTPS 설정은 생략
BASE_URL = "http://localhost:8000"

def get_welcome_message():
    """Get the API welcome message"""
    response = requests.get(f"{BASE_URL}/")
    print("\n1. Welcome Message:")
    print(response.json())

def get_cities():
    """Get list of all available cities"""
    response = requests.get(f"{BASE_URL}/cities")
    print("\n2. Available Cities:")
    print(response.json())

def get_weather(city):
    """Get weather for a specific city"""
    response = requests.get(f"{BASE_URL}/weather/{city}")
    print(f"\n3. Weather for {city}:")
    print(response.json())

# Test all endpoints
try:
    # 1. Get welcome message
    get_welcome_message()

    # 2. Get list of cities
    get_cities()

    # 3. Get weather for 서울
    get_weather("서울")

except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Error details: {e.response.json()}")