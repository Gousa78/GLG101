import urllib.request
import json
import turtle
import time
"""
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# print(result)

people = result['people']
for p in people:
    print(p['name'], 'in craft', p['craft'])
"""
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])


# lat = float()
# lon = float()


screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.png")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(90)

#  turtle.done()


iss.penup()
print('Latitude: ', lat)
print('Longitude: ', lon)
iss.goto(lat, lon)
# iss.goto(0, 0)

screen.exitonclick()

# turtle.done()