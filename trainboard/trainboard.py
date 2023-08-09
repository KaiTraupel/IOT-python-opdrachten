import http.client
import json
from datetime import datetime

# url voor de data die nodig is voor het liveboard van Antwerpen-Centraal
url = "/liveboard/?station=Antwerpen-Centraal&arrdep=departure&lang=nl&format=json&alerts=false"

conn = http.client.HTTPSConnection("api.irail.be")
conn.request("GET", "/liveboard/?station=Antwerpen-Centraal&arrdep=departure&lang=nl&format=json&alerts=false")
res = conn.getresponse()
data = res.read().decode("utf-8")



