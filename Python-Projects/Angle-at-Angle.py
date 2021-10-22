# ref: https://cppsecrets.com/users/5440112114971061011151044611511410511897115116971189795991154956641031089746979946105110/Python-turtle-Angle-at-Angle-Project.php

from turtle import *
import turtle
turtle.Turtle()
for angle in range(0, 360, 15):
    setheading(angle)
    forward(100)
    write(str(angle) + '�')
    backward(100)
turtle.done()