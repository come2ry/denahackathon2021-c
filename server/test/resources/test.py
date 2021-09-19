import pytest
from app import app
import json
from flask import url_for


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_sample(client):
    result = client.post(f'{app.config["API_PREFIX"]}/geo', data={"geo":{"user_id": 12, "latitude": 35.6075, "longitude": 139.6856 }})
    # assert result.get_json() == []
    print(result.get_json())
    assert result.status_code == 200

    result = client.get(f'{app.config["API_PREFIX"]}/geo?top=30.54521&left=135.6543&bottom=30.4000&right=135.88888')
    # assert result.get_json() == []
    print(result.get_json())
    assert result.status_code == 200


    result = client.post(f'{app.config["API_PREFIX"]}/locus', data={"user_id": 12, "locus": [
        {"latitude": 35.6075, "longitude": 139.6860 },
        {"latitude": 35.6080, "longitude": 139.6855 },
        {"latitude": 35.6075, "longitude": 139.6850 },
        {"latitude": 35.6070, "longitude": 139.6855 }
    ]})
    # assert result.get_json() == []
    print(result.get_json())
    assert result.status_code == 200

    locus_id = 1
    print(f'{app.config["API_PREFIX"]}/locus/{locus_id}')
    result = client.get(f'{app.config["API_PREFIX"]}/locus/{locus_id}')
    # assert result.get_json() == []
    print(result.get_json())
    assert result.status_code == 200
