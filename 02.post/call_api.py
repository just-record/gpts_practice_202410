import requests

# API base URL
### 실제 GPTs의 API로 사용 하기 위해서는 HTTPS여야 함 - HTTPS 설정은 생략
BASE_URL = "http://localhost:8000"

def get_weather(city):
    """Get weather for a specific city"""
    # POST 요청을 위한 데이터 준비
    data = {"city": city}
    
    # POST 요청 보내기
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/weather",
        json=data,
        headers=headers
    )
    
    print(f"\nWeather for {city}:")
    print(response.json())

# Test all endpoints
try:
    get_weather("서울")

except requests.exceptions.RequestException as e:
    print(f"Error occurred: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Error details: {e.response.json()}")