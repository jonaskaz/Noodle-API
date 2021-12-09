from threading import current_thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import GAME_MODE, ORDER_MODE
from pydantic import BaseModel
from typing import Optional
import queue



class Payload(BaseModel):
    mode: int
    flavor: str
    toppings: Optional[list] = []


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://cup-noodle-app.herokuapp.com",
    "https://cup-noodle-app.herokuapp.com",
    "cup-noodle-app.herokuapp.com",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

orders = queue.Queue()

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome"}

@app.get("/order", tags=["orders"])
async def get_order() -> dict:
    if orders.empty():
        current_order = {}
    else:
        current_order = orders.get()
    return current_order

@app.post("/order", tags=["orders"])
async def post_order(order: Payload) -> dict:
    orders.put(order)
    return {
        "data": { "Order successfully posted." }
    }

