import pytest
from app import app
import json
from flask import url_for


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_sample(client):
    result = client.get(
        f'{app.config["API_PREFIX"]}/sample/users')
    assert result.get_json() == [
        {
            'birthday': None, 'github_id': 'yud0uhu', 'role': 'frontend'}, {
            'birthday': None, 'github_id': 'bababax11', 'role': 'frontend'}, {
                'birthday': 'Wed, 09 Dec 1998 00:00:00 GMT', 'github_id': 'come2ry', 'role': 'backend'}, {
                    'birthday': None, 'github_id': 'maruyu998', 'role': 'backend'}, {
                        'birthday': None, 'github_id': 'ari1021', 'role': 'backend'}]
    assert result.status_code == 200

    SAMPLE_ID = 1
    print(f'/api/v1/sample/users/{SAMPLE_ID}')

    result = client.get("/api/v1/sample/users/1")
    assert result.get_json() == [
        {'birthday': None, 'github_id': 'yud0uhu', 'role': 'frontend'}]
    assert result.status_code == 200

    SAMPLE_DATA = {
        "github_id": "hoge",
        "birthday": "1111-11-11",
        "role": "backend",
    }
    result = client.post(
        f'{app.config["API_PREFIX"]}/sample/users',
        data=json.dumps(SAMPLE_DATA))

    assert result.get_json() == SAMPLE_DATA
    assert result.status_code == 200

    SAMPLE_QUERY = {
        "github_id": "hoge"
    }
    SAMPLE_QUERY_STRING = "&".join(
        [f"{k}={v}" for k, v in SAMPLE_QUERY.items()])
    result = client.get(
        f'{app.config["API_PREFIX"]}/sample/users?{SAMPLE_QUERY_STRING}')
    assert result.get_json()[0] == SAMPLE_DATA
    assert result.status_code == 200
