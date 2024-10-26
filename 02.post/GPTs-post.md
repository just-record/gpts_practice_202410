# GPTs 기본 연습 - 날씨 정보 API

## GPTs 생성하기

- Name: `Get Weather information 2`
- Description: `Get the weather information for a given city`
- Instructions:

```plaintext
**Context**: A user needs information related to the current weather of a specific city.

**Instructions**:
1. The user will provide a city name or a related landmark (e.g. Eiffel Tower, New York City). If the user does not provide one, ask for the relevant city or landmark.
2. If the user provides a landmark, convert it into the corresponding city name. If required, browse the web to verify the correct location.
3. Use a weather API to retrieve the current weather for the given city.
4. Present the relevant weather data (such as temperature, conditions, humidity, wind speed, etc.) in an easily understandable format for the user.
5. When calling API, the city name must be called in Korean.

**Additional Notes**:
- Assume the user prefers Korea weather units (e.g. Celsius) unless otherwise specified.
- If the user asks for specific weather details (e.g. rainfall, humidity, or wind speed), include those elements in your response.
- If the user says "Let's get started" or "What do I do?", explain the purpose of this Custom GPT and ask them to provide the name of the city or landmark.
```

## GPTs Action schema 생성

- OpenAI의 공식 GPTs: Actions 스키마 생성해 주는 GPTs
- <https://chatgpt.com/g/g-TYEliDU6A-actionsgpt>

✔️ 요청

```python
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


의 Action schema를 생성 해 줘
```

✔️ 결과

- 아래의 url은 HTTPS여야 함 - HTTPS 설정은 생략

```yaml
openapi: 3.1.0
info:
  title: Weather API
  description: API for retrieving weather information for a specific city.
  version: 1.0.0
servers:
  - url: https://localhost:8000
    description: Main production server
paths:
  /weather:
    post:
      operationId: getWeather
      summary: Get weather for a specific city
      description: Retrieves the current weather for a provided city.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                city:
                  type: string
                  description: The name of the city to retrieve weather for
              required:
                - city
      responses:
        '200':
          description: Successfully retrieved weather information
          content:
            application/json:
              schema:
                type: object
                properties:
                  temperature:
                    type: number
                    format: float
                    description: Current temperature in the city
                  humidity:
                    type: integer
                    description: Current humidity percentage in the city
                  description:
                    type: string
                    description: A short description of the weather
        '400':
          description: Bad Request - Invalid city parameter
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message describing what went wrong
        '500':
          description: Server Error - Something went wrong on the server
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message explaining server failure
```

## GPTs Action schema 등록

- Action: `create new action`
  - Authentication: None
  - Schema: 위에서 생성한 Open API 스키마
  - Privacy policy: 생략 (아래에서 Only me 선택)

- `Create` -> Option 선택 ( Only me / Anyone with the link / GPT Store)

## 테스트

- API 서버가 실행 된 상태
- 생성된 GPTs(Get Weather information) 이동

✔️ What is the weather like in Seoul?

```plaintext
The current weather in Seoul is as follows:
Temperature: 15°C
Conditions: Clear (맑음)
Humidity: 55%
Wind Speed: 8 km/h
Precipitation: 0 mm
Air Quality: Moderate (보통)
Sunrise: 6:45 AM
Sunset: 5:45 PM
This data was last updated today at 10:00 AM. Let me know if you'd like more details!
```

✔️ 부산의 날씨는?

```plaintext
부산의 현재 날씨는 다음과 같습니다:
기온: 19.5°C
날씨: 눈
습도: 75%
풍속: 12 km/h
강수량: 5 mm
미세먼지: 좋음
일출: 오전 6:35
일몰: 오후 5:35
이 데이터는 오늘 오전 10시에 업데이트되었습니다. 추가 정보가 필요하시면 말씀해 주세요!
```

✔️ 엑스코의 날씨는?

```plaintext
엑스코(EXCO)는 대구에 위치한 컨벤션 센터입니다. 대구의 날씨 정보를 가져오겠습니다.

엑스코가 위치한 대구의 현재 날씨는 다음과 같습니다:
기온: 18°C
날씨: 구름 조금
습도: 60%
풍속: 6 km/h
강수량: 0 mm
미세먼지: 좋음
일출: 오전 6:40
일몰: 오후 5:40
이 정보는 오늘 오전 10시에 업데이트되었습니다. 다른 정보가 필요하시면 알려주세요!
```