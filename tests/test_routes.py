

def test_post_order(client, order_payload):
    res = client.post("/order", json = order_payload)
    assert res.status_code == 200


def test_post_game(client, game_payload):
    res = client.post("/order", json = game_payload)
    assert res.status_code == 200


def test_get_order(client):
    res1 = client.get("/order")
    assert res1.json()["mode"] == 0
    assert res1.json()["toppings"] == ["onions", "spice"]
    res2 = client.get("/order")
    assert res2.json()["mode"] == 1
    res3 = client.get("/order")
    assert res3.json() == {}
