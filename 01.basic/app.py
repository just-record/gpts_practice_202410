from fastapi import FastAPI, HTTPException
from typing import Dict, List, Optional
from datetime import datetime
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="Simple Weather API")

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

class WeatherUpdate(BaseModel):
    temperature: float
    humidity: int
    conditions: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather API"}

@app.get("/weather/{city}")
def get_weather(city: str):
    if city not in weather_data:
        raise HTTPException(status_code=404, detail="City not found")
    return weather_data[city]

@app.get("/cities")
def get_cities():
    return list(weather_data.keys())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)