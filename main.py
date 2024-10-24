from fastapi import FastAPI

app = FastAPI() # FastAPI의 인스턴스 객체 app를 생성. 


@app.get("/")       # 경로 동작 데코레이터 (url 주소)
async def root():   # 경로 동작 함수
    return {"message": "Hello GPTs Practice"} # json Type으로 return