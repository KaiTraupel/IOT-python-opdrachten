import http.client as website
import json
from datetime import datetime

url = "/liveboard/?station=Antwerpen-Centraal&arrdep=departure&lang=nl&format=json&alerts=false"

conn = website.HTTPSConnection("api.irail.be")
payload = ""
headers = {}

conn.request("GET", url, payload, headers)
res = conn.getresponse()

data = json.loads(res.read())

# print(data)

ts = int('1691517687')

print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))



