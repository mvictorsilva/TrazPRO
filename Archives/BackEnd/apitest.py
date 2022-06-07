import requests


url = "https://api.linketrack.com/track/json?" \
      "user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&" \
      "codigo=QJ331080523BR"

payload = {}
headers = {}

request = requests.request("GET", url, headers=headers, data=payload)
request = request.json()

# print(request['eventos'][2])

reques = request['eventos']

for r in reques:
#     print(r)
    for i in r.values():
        print(i)
