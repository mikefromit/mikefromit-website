def test_home_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert '<title>Home | mikefromit website</title>' in response
