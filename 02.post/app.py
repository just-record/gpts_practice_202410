from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Simple Weather API")

### 추가된 부분
# Pydantic 모델 정의
class WeatherRequest(BaseModel):
    city: str

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


### 수정된 부분
@app.post("/weather")
def get_weather(request: WeatherRequest):
    if request.city not in weather_data:
        raise HTTPException(status_code=404, detail="City not found")
    return weather_data[request.city]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)