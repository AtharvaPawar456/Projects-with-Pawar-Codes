# ref: https://cppsecrets.com/users/5440112114971061011151044611511410511897115116971189795991154956641031089746979946105110/Python-turtle-Circle-Mania-Project.php

import turtle
pawar = turtle.Screen()
pawar.bgcolor('black')
s = turtle.Turtle()
s.speed('fastest')
s.color('white')
rotate=int(180)
def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def pawara(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)
pawara(s,200,10)
t1 = turtle.Turtle()
t1.speed(0)
t1.color('yellow')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def pawarb(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
pawarb(t1,160,10)
t2= turtle.Turtle()
t2.speed(0)
t2.color('blue')
rotate=int(80)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def pawarc(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
pawarc(t2,120,10)
t3 = turtle.Turtle()
t3.speed(0)
t3.color('red')
rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def paward(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
paward(t3,80,10)
t4= turtle.Turtle()
t4.speed(0)
t4.color('green')

rotate=int(90)
def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def paware(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
paware(t4,40,10)
turtle.done()