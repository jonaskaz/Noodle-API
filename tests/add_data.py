import requests
import time

url = "https://cup-noodle-api.herokuapp.com/order"
order_json = {
        "mode": 0,
        "flavor": "beef",
        "toppings": ["onions", "spice"]
    }

game_json = {
        "mode": 1,
        "flavor": "beef"
    }

for i in range(10):
    r = requests.post(url, json=order_json)
    assert r.status_code == 200
    r = requests.post(url, json=game_json)
    assert r.status_code == 200
    time.sleep(0.5)
