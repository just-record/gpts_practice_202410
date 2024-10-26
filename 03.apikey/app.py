from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Simple Weather API")

### 추가된 부분
# Security scheme 설정
security = HTTPBearer()

### 추가된 부분
# API 키 설정 (실제 환경에서는 환경 변수나 보안 저장소에서 관리해야 함)
API_KEY = "your-secure-api-key-here"

# Pydantic 모델 정의
class WeatherRequest(BaseModel):
    city: str


### 추가된 부분
# 인증 확인 함수
async def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    print(credentials)
    print(credentials.credentials)
    print(API_KEY)
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials    

# Sample weather data storage
weather_data = {
    "서울": {
        "temperature": 15,  # Typical autumn temperature
        "humidity": 55,     # Moderate humidity
        "conditions": "맑음",
        "wind_speed": 8,    # km/h
        "precipitation": 0,  # mm
        "air_quality": "보통",
        "last_updated": "2024-10-25T10:00:00",
        "sunrise": "2024-10-25T06:45:00",
        "sunset": "2024-10-25T17:45:00"
    },
    "대구": {
        "temperature": 18,  # Usually warmer than Seoul
        "humidity": 60,
        "conditions": "구름 조금",
        "wind_speed": 6,    # km/h
        "precipitation": 0,  # mm
        "air_quality": "좋음",
        "last_updated": "2024-10-25T10:00:00",
        "sunrise": "2024-10-25T06:40:00",
        "sunset": "2024-10-25T17:40:00"
    },
    "부산": {
        "temperature": 19,  # Coastal climate influence
        "humidity": 65,
        "conditions": "구름많음",
        "wind_speed": 12,   # km/h
        "precipitation": 5,  # mm
        "air_quality": "좋음",
        "last_updated": "2024-10-25T10:00:00",
        "sunrise": "2024-10-25T06:35:00",
        "sunset": "2024-10-25T17:35:00"
    }
}



@app.post("/weather")
# def get_weather(request: WeatherRequest):
async def get_weather(request: WeatherRequest, token: str = Depends(verify_token)):    ### 수정된 부분
    if request.city not in weather_data:
        raise HTTPException(status_code=404, detail="City not found")
    return weather_data[request.city]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)