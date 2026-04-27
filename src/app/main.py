from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Model(BaseModel):
    id: str
    name: str
    version: str
    snapshot_path: str

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/alive")
def read_alive():
    return {"OK": True}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

@app.put("/model")
def create_model(model: Model):
    return model