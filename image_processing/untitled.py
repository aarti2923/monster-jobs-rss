import requests
from ast import literal_eval
import json
headers = {'Content-Type':"application/json"}
info = requests.get('http://192.168.0.145:8000/api/rss_data/?cat_id=907', headers=headers).json()
# info = info.split('response')[1]
print(info['response'])