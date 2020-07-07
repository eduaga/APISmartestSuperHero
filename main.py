import requests as req
from pprint import pprint

BASE_URL_TOKEN_CONST = "https://www.superheroapi.com/api.php/2619421814940190"


def get_intelligence(*super_heros):
    the_smartest = ''
    intelligence = 0
    for hero in super_heros:
      resp = req.get(f'{BASE_URL_TOKEN_CONST}/search/{hero}').json()
      super_hero_id = resp['results'][0]['id']
      resp = req.get(f'{BASE_URL_TOKEN_CONST}/{super_hero_id}/powerstats').json()
      super_hero_intelligence = int(resp['intelligence'])
      if super_hero_intelligence > intelligence:
        the_smartest = hero
        intelligence = super_hero_intelligence
    print(f'Самый умный супергерой - {the_smartest}')



get_intelligence('Thanos', 'Captain%20America', 'Hulk')
