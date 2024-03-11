import requests
import random

def show_list(list, title):
    print(f'{title}:')
    for item in list:
        print(f' — {item}')

page = 5482 # random.randint(1, 7438)
pageSize = 1
url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'
response = requests.get(url)
if response.ok:
    as_json = response.json()['data']
    print(as_json['name'])

    show_list(as_json['films'], 'Films')
    show_list(as_json['tvShows'], 'TV Shows')
    show_list(as_json['videoGames'], 'Video Games')

else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')