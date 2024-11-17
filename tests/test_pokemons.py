import requests
import pytest

URl = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c6be9777b2ac0e589b02c17b11d5609'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 7265

def test_status_code():
    response = requests.get(url = f'{URl}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URl}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'бульбозавр'