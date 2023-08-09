import http.client
import json
import turtle
from datetime import datetime

# url voor de data die nodig is voor het liveboard van Antwerpen-Centraal
url = "/liveboard/?station=Antwerpen-Centraal&arrdep=departure&lang=nl&format=json&alerts=false"

# verbinding maken met iRail API
conn = http.client.HTTPSConnection("api.irail.be")
conn.request("GET", "/liveboard/?station=Antwerpen-Centraal&arrdep=departure&lang=nl&format=json&alerts=false")
res = conn.getresponse()
data = res.read().decode("utf-8")
conn.close()

# data in meer leesbare json vorm steken
data = json.loads(data)

# lijst van alle vertrekkende treinen en hun info
informatie = data.get("departures", {}).get("departure", [])









ttl = turtle.Turtle()

def balk_tekenen(x, y,):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()

