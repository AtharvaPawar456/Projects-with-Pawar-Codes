#Python Program to draw Audi logo in Turtle Programming
import turtle
 
t = turtle.Turtle()
t.pensize(8)
 
for i in range(4):
  t.penup()
  t.goto(i*70, 0)
  t.pendown()
  t.circle(50)

turtle.done()