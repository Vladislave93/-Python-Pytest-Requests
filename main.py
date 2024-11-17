import requests

URl = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c6be9777b2ac0e589b02c17b11d5609'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "vlad@yandex.ru",
    "password": "SloverS"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "бульбозавр",
    "photo_id": 1
}
body_edit = {
    "pokemon_id": "136811",
    "name": "generate",
    "photo_id": -1
}
body_catch = {
    "pokemon_id": "136811"
}

#регистрация тренера
'''response = requests.post(url = f'{URl}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

#подтверждение почты
'''response_confirmation = requests.post(url = f'{URl}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

#создание покемона 
'''response_create= requests.post(url = f'{URl}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

#смена имени покемона 
'''response_edit = requests.put (url = f'{URl}/pokemons', headers = HEADER, json = body_edit)
print(response_edit.text)

message = response_edit.json()['message']
print(message)'''

#поймать в покебол
'''response_catch = requests.post (url = f'{URl}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

message = response_catch.json()['message']
print(message)'''
