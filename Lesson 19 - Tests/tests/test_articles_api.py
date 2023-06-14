def test_get_articles_list(client):
    response = client.get("http://nginx/api/articles")
    assert response.status_code == 200
    assert response.json[0].get("id") == 1


def test_create_article(client):
    response = client.post("http://nginx/api/articles", json={
        "title": "hello",
        "body": "hello hello hello"
    })
    assert response.status_code == 200
    assert response.json.get("title") == "hello"