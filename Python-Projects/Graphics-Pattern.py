#ref: https://cppsecrets.com/users/5440112114971061011151044611511410511897115116971189795991154956641031089746979946105110/Python-turtle-Graphics-Pattern-project.php

import turtle
t = turtle.Turtle()
list1 = ["purple","red","orange","blue","green"]
turtle.bgcolor("black") 
for i in range(200):
    t.color(list1[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)
turtle.done()