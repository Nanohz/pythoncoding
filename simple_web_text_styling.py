#!/bin/python3
from turtle import *

screen = Screen()
screen.setup(400, 400)

colours = {'lime' : '#A7E30E', 'reallyrasberry': '#FA057F'}
screen.bgcolor(' #004d00')

color(colours['lime'])
style = ('Arial', 40, 'bold')
write('Hello' , font = style, align= 'center')
hideturtle()

print(colours [ 'lime'])
print(colours ['reallyrasberry'])
