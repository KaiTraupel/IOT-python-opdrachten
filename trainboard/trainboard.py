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








# rechthoek tekenen
ttl = turtle.Turtle()
def balk_tekenen(breedte, hoogte, kleur):
    ttl.pendown()
    ttl.speed(0)
    turtle.tracer(0, 0)
    ttl.begin_fill()
    ttl.fillcolor(kleur)
    for i in range(2):
        ttl.forward(breedte)
        ttl.right(90)
        ttl.forward(hoogte)
        ttl.right(90)
    ttl.end_fill()
    ttl.penup()

    ttl.forward(breedte)
    
    

# tekenpositie linksboven
x_position = -turtle.window_width() / 2
y_position = turtle.window_height() / 2

# breedte en hoogte van de balken
width = turtle.window_width() / 3
height = turtle.window_height() / 9

# start positie
ttl.penup()
ttl.goto(x_position, y_position)

for i in range(3):
    balk_tekenen(width, height, "blue")

turtle.update()
turtle.done()



