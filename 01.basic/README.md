# 기본 API 서버

- 날씨를 제공하는 API 서버를 구축
- 지역은 서울, 대구, 부산을 제공
- endpoint:
    - `/`: Welcome message
    - `/weather/{city}`: 해당 도시의 날씨 정보
    - `/cities`: 제공하는 도시 목록

## 실행 방법

✔️ 서버

```bash
python app.py
```

✔️ API 호출

```bash
python call_api.py
```

## GPTs 작성

- GPTs-basic.md

## 주의사항

코드에는 http://localhost:8000으로 설정되어 있지만 실제 GPTs의 API 서버는 **HTTPS**로 서비스 되어야 함.

