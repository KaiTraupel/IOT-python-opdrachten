import http.client
import json
import turtle
from datetime import datetime
ttl = turtle.Turtle()

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

# tekenpositie linksboven
x_position = -turtle.window_width() / 2
y_position = turtle.window_height() / 2

# info
vertrek_tijd = []
bestemming = []
trein_type = []
platform = []
vertraging = []

# afgaan van alle vertrekkende treinen en info opslaan in lijsten
for departure in data["departures"]["departure"]:
    tijd = int(departure["time"]) # tijd opslaan als int om hieronder te kunne omzetten naar u en min
    tijd = datetime.fromtimestamp(tijd).strftime("%H:%M")
    vertrek_tijd.append(tijd)
    bestemming.append(departure["stationinfo"]["name"])
    trein_type.append(departure["vehicleinfo"]["type"])
    platform.append(departure["platform"])
    delay = int(departure["delay"])
    vertraging.append(int(delay / 60))
    

print(vertraging)

 # rechthoek tekenen en de informatie erin zetten
def balk_tekenen(breedte, hoogte, kleur, info):
    ttl.color("white")
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
    ttl.forward(width)
    pos = ttl.pos()
    ttl.backward(breedte - 15)
    ttl.right(90)
    ttl.forward(40)
    ttl.left(90)
    ttl.write(f"{vertrek_tijd[info]}", font=("Arial", 14, "normal"))
    ttl.forward(breedte / 4)
    if vertraging[info] > 0:
        ttl.color("red")
        ttl.write(f"+ {vertraging[info]}", font=("Arial", 14, "normal"))
        ttl.color("white")
    ttl.forward(breedte / 3)
    ttl.write(f"{trein_type[info]}", font=("Arial", 14, "normal"))
    ttl.forward(breedte / 5)
    ttl.write(f"{platform[info]}", font=("Arial", 14, "normal"))
    ttl.goto(pos)
    ttl.backward(breedte - 15)
    ttl.right(90)
    ttl.forward(70)
    ttl.left(90)
    ttl.write(f"{bestemming[info]}", font=("Arial", 14, "normal"))
    ttl.goto(pos)
    

print(vertrek_tijd)  

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

# gebruiken om de info van de volgende treinen op te halen
info = 0

# loop die een rooster maakt van drie kolommen en negen rijen
for i in range(9):
    for i in range(3):
        cellen = cellen + 1
        print(info)
        balk_tekenen(width, height, kleuren[(cellen % 2)], info)
        if info < 20:
            info = info + 1
    ttl.goto(x_position, y_position - (height * rij))
    rij = rij + 1


turtle.update()
turtle.done()



