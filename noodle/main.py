from fastapi import FastAPI
from .config import GAME_MODE, ORDER_MODE
from pydantic import BaseModel
from typing import Optional
import queue


class Payload(BaseModel):
    mode: int
    flavor: str
    toppings: Optional[list] = None


app = FastAPI()
order_q = queue.Queue()


@app.get("/")
def root():
    return {"message": "Welcome"}


@app.post("/order")
def create_order(payload: Payload):
    order_q.put(payload)
    return payload


@app.get("/order")
def get_latest_order():
    if order_q.empty():
        order = {}
    else:
        order = order_q.get()
    return order

