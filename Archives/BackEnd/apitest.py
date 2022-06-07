import requests
import json

url = "https://api.linketrack.com/track/json?" \
      "user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&" \
      "codigo=QJ331080523BR"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

res = response.text.encode('utf8')

print(type(res))
print(res)
