from hashlib import new
import requests
from pprint import pprint
import json

url = "https://api.linketrack.com/track/json?" \
      "user=teste&" \
      "token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&" \
      "codigo=QJ331080523BR"
      

request = requests.get(url)
reques = request.json()

# pprint(reques)

reque = reques['eventos']

for pontos in reque:
     for valores in pontos:
         print(pontos[valores])    
