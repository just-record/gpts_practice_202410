# GPTs 기본 연습 - 날씨 정보 API

## GPTs 생성하기

- Name: `Get Weather information`
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

- OpenAI의 공식 GPTs: Actions 스키마 생성

✔️ 요청

```python
def get_weather(city):
    """Get weather for a specific city"""
    response = requests.get(f"{BASE_URL}/weather/{city}")
    print(f"\n3. Weather for {city}:")
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

- 실제 나온 결과에서 조금 수정 함. -> 테스트 과정에서 수정이 필요했고 거의 그대로 사용 가능 했음.
- 아래의 url은 HTTPS여야 함 - HTTPS 설정은 생략

```yaml
openapi: 3.1.0
info:
  title: Weather information API
  description: This API provides weather information for various cities
  version: 1.0.0
servers:
  - url: https://localhost:8000
    description: Main production server

paths:
  /weather/{city}:
    get:
      operationId: getWeather
      summary: Get weather for a specific city.
      description: Fetches the weather information for a specified city. The city name must be called in Korean.
      parameters:
        - name: city
          in: path
          required: true
          description: Name of the city to retrieve weather data for.
          schema:
            type: string
      responses:
        '200':
          description: Weather data for the specified city.
          content:
            application/json:
              schema:
                type: object
                properties:
                  city:
                    type: string
                    description: Name of the city.
                  temperature:
                    type: number
                    format: float
                    description: Temperature in the city.
                  condition:
                    type: string
                    description: Current weather condition in the city.
                required:
                  - city
                  - temperature
                  - condition
        '404':
          description: City not found.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: Error message when the city is not found.
                required:
                  - error
```

## GPTs Action schema 등록

- Action: `create new action`
  - Authentication: None
  - Schema: 위에서 생성한 Open API 스키마
  - Privacy policy: <https://app.example.com/privacy> - 존재하지 않는 링크

✔️ Privacy policy - 개인정보 처리방침

- Only me로 적용 할 경우 입력하지 않아도 됨
- 존재하지 않는 링크를 입력 해도 저장은 가능 함: 실 사용시에는 정확한 Privacy policy를 입력 해야 하고 진행 해야 함
- 아래는 GPT에게 Privacy policy에 대한 문의의 답

```markdown
### Why the Privacy Policy is Important
A privacy policy is a legal document that explains how you, as a service provider or developer, collect, use, store, and protect user data. Many platforms require it to ensure transparency and comply with data protection regulations, such as the General Data Protection Regulation (GDPR) in Europe or the California Consumer Privacy Act (CCPA) in the U.S.

When you integrate an API or app with a platform, it's essential to show users how their data will be handled. For instance, if your service collects personally identifiable information (PII) like emails, names, or user preferences, the privacy policy should state:

- What data is collected (e.g., name, location, browsing behavior).
- How the data is used (e.g., for improving services, marketing, analytics).
- How long the data is retained.
- Whether the data is shared with third parties.
- User rights (e.g., access to their data, deletion requests).
- Contact information if users have concerns about their privacy.

### Example Privacy Policy

Here’s an example of what you might include:

- What data we collect: We collect email addresses and usage data.
- How we use your data: We use your email to send important updates about our service, and usage data to improve our user experience.
- Data sharing: We don’t share your data with third parties, except for essential service providers such as payment processors or analytics platforms.
- Data retention: Your data is stored for as long as your account remains active or as required by law.
- User rights: You can request the deletion or modification of your data at any time.
- Contact: For questions about your privacy, please reach out to us at privacy@yourapp.com.
```

- `CreateAction` -> Option 선택 ( Only me / Anyone with the link / GPT Store)
- GPTs: <https://chatgpt.com/g/g-1Q97lKKWN-get-weather-information>

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
Let me know if you need more details!
```

✔️ 부산의 날씨는?

```plaintext
현재 부산의 날씨는 다음과 같습니다:
기온: 19.5°C
날씨: 눈
습도: 75%
풍속: 12 km/h
강수량: 5 mm
미세먼지: 좋음
일출: 오전 6:35
일몰: 오후 5:35
추가 정보가 필요하시면 말씀해 주세요!
```

✔️ 부산의 날씨는?

```plaintext
엑스코(EXCO)는 대구에 위치한 컨벤션 센터입니다. 대구의 날씨 정보를 가져오겠습니다.

현재 대구(엑스코)의 날씨는 다음과 같습니다:
기온: 18°C
날씨: 구름 조금
습도: 60%
풍속: 6 km/h
강수량: 0 mm
미세먼지: 좋음
일출: 오전 6:40
일몰: 오후 5:40
다른 정보가 필요하시면 알려주세요!
```