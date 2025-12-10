# Requisições HTTP com Python
import requests

print('Github Users\n')
usarname = input('Qual o nome de usuário? ')

url = f'https://api.github.com/users/{usarname}'

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    print(f'\nNome completo: {data["name"]}')
    print(f'Bio: {data["bio"]}')
    print(f'Localização: {data["location"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
else:
    print('Não foi possivel encontrar o usuário!')
