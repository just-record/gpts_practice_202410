# Post 방식의 API 서버

- 02.basic과 거의 동일 함
- API-KEY를 사용하는 인증을 추가 함(Bearer Token)

## 실행 방법

✔️ 서버

```bash
python app.py
```

✔️ API 호출 테스트

```bash
python call_api.py
```

## GPTs 작성 및 테스트

- GPTs-apikey.md

## 주의사항

코드에는 http://localhost:8000으로 설정되어 있지만 실제 GPTs의 API 서버는 **HTTPS**로 서비스 되어야 함.

