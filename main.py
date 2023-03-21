from typing import Union

from fastapi import FastAPI

app = FastAPI()
from fastapi.responses import FileResponse

@app.get("/")
def read_root():
    return FileResponse('index.html')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}