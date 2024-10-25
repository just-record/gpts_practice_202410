# Post 방식의 API 서버

- 01.basic과 거의 동일 함
- `get`방식이 아닌 `post`방식으로 변경 하여 도시의 날씨 정보를 제공

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

- GPTs-post.md

## 주의사항

코드에는 http://localhost:8000으로 설정되어 있지만 실제 GPTs의 API 서버는 **HTTPS**로 서비스 되어야 함.

