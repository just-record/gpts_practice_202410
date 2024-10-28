# `x-openai-isConsequential`

## Consequential flag

<https://platform.openai.com/docs/actions/production/consequential-flag>

예를 들어 사용자를 대신해서 호텔 객실을 예약하고 결제한다면 자동으로 처리 하는게 나을까요? 사용자의 동의를 받도록 하는게 나을까요?

- x-openai-isConsequential: true
  - ChatGPT는 "실행하기 전에 반드시 사용자의 확인을 받아야 함"으로 처리
  - "항상 허용" 버튼을 표시하지 않음
- x-openai-isConsequential: false
  - ChatGPT는 "항상 허용" 버튼을 표시
  - "항상 허용" 버튼을 클릭하면 다음 부터는 사용자 동의 없이 자동으로 처리
- 이 필드가 없는 경우
  - 모든 GET 작업: 기본값 - false
  - 다른 모든 작업: true

## 작성 예시

```yaml
paths:
  /todo:
    get:
      operationId: getTODOs
      description: Fetches items in a TODO list from the API.
      security: []
    post:
      operationId: updateTODOs
      description: Mutates the TODO list.
      x-openai-isConsequential: true
```      

- 원하는 모든 Action에 대해 각각 `x-openai-isConsequential`을 설정할 수 있음

## 참고

<https://community.openai.com/t/how-to-stop-custom-gpt-displaying-confirm-deny-buttons/874551>

