import requests

# API base URL
### 실제 GPTs의 API로 사용 하기 위해서는 HTTPS여야 함 - HTTPS 설정은 생략
BASE_URL = "http://localhost:8000"

def get_weather(city):
    """Get weather for a specific city"""
    response = requests.get(f"{BASE_URL}/weather/{city}")
    print(f"\n Weather for {city}:")
    print(response.json())

# Test all endpoints
try:
    get_weather("서울")

except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Error details: {e.response.json()}")