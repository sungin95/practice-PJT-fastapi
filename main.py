from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# 1단계를 공부하고
# fastapi는 장고랑 다르게 async 기능이 있다. 이 덕분에 nodeJS처럼 속도가 빠르다고 한다. 
# 그렇다면 이 async는 어느 상황에 사용해야 되는 걸까? 