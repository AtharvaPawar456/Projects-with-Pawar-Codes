#ref: https://cppsecrets.com/users/5440112114971061011151044611511410511897115116971189795991154956641031089746979946105110/Python-turtle-Cyclic-Project.php

import turtle
pawar = turtle.Screen()
pawar.bgcolor("black")
Python = turtle.Turtle()
Python.shape("turtle")
Python.color("red")

Python.penup()
pawarplus = 20
for i in range(30):
   Python.stamp()            
   pawarplus = pawarplus + 3          
   Python.forward(pawarplus)   
   Python.right(24)           

pawar.mainloop()
turtle.done()