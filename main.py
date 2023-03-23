from fastapi import FastAPI
from enum import Enum

app = FastAPI()


# 이건 왜 request가 없지???
@app.get("/")
async def root():
    return {"message": "Hello World"}


# 1단계를 공부하고
# fastapi는 장고랑 다르게 async 기능이 있다. 이 덕분에 nodeJS처럼 속도가 빠르다고 한다.
# 그렇다면 이 async는 어느 상황에 사용해야 되는 걸까?


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# me가 먼저 오지 않으면 실행이 안된다. 이건 장고랑 동일
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# Enum를 사용해서 아래와 같이 만들면 특정 단어만 받을 수 있다.
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# 이건 무슨 말이지?
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# a번째부터 b번쨰 까지
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


Union = "마마"


# 퀴리 매개변수의 타입을 미리 지정 할 수 있다.
# 퀴리 매개변수란 파라미터를 통해 전달된 값
# needy: str 이렇게 기본값을 지정 안하면 필수가 된다.
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
