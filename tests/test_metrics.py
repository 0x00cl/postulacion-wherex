def test_get_metrics(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.json.get("cpu").get("percent") is not None
    assert response.json.get("cpu").get("times") is not None
    assert response.json.get("cpu").get("stats") is not None
    assert response.json.get("memory").get("virtual_mem") is not None
    assert response.json.get("memory").get("swap_mem") is not None
