import main

def test_hello():
    client = main.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World' in response.data
