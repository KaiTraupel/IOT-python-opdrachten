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

# afgaan van alle vertrekkende treinen en info uithalen
for departure in data["departures"]["departure"]:
    vertrek_tijd = departure["time"]
    bestemming = departure["stationinfo"]["name"]
    trein_naam = departure["vehicleinfo"]["shortname"]



















# rechthoek tekenen
ttl = turtle.Turtle()
def balk_tekenen(breedte, hoogte, kleur):
    ttl.pendown()
    ttl.hideturtle()
    ttl.begin_fill()
    turtle.tracer(0,0)
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

# nodig voor het aantal rijen te bepalen in vollgende loop
rij = 1

# aantal cellen te tellen, nodig voor kleuren te laten afwisselen
cellen = 0

# kleuren voor de cellen
kleuren = ["blue", "darkblue"]

# loop die een rooster maakt van drie kolommen en negen rijen
for i in range (9):
    for i in range(3):
        cellen = cellen + 1
        balk_tekenen(width, height, kleuren[(cellen % 2)])
    ttl.goto(x_position, y_position - (height * rij))
    rij = rij + 1



turtle.update()
turtle.done()



