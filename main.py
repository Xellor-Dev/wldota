import requests
import json
api_key = '' #https://www.opendota.com/api-keys
url = 'https://api.opendota.com/api/'

account_id = '' #Steam 32 ID
wl_url = f"players/{account_id}/wl"

response = requests.get(url + wl_url, params={'api_key': api_key})

if response.status_code == 200:
    json_data = response.json()
    win = json_data['win']
    lose = json_data['lose']
    print(f'Win: {win}')
    print(f'Lose: {lose}')
else:
    print('Eror:', response.status_code)