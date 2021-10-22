import turtle
Cppsecrets = turtle.Turtle()
s=turtle.Screen()
turtle.screensize(1400,1400)
Cppsecrets.pencolor("red")
Cppsecrets.write("Stay Home Stay Safe ",'false','center',font=('Showcard gothic',40))
s.bgcolor("black")
Cppsecrets.pencolor("dark green")
Cppsecrets.pensize(2)
Python=0
CplusPlus=0
Cppsecrets.speed(0)
Cppsecrets.penup()
Cppsecrets.goto(0,560)
Cppsecrets.pendown()
while True:
    Cppsecrets.forward(Python)
    Cppsecrets.right(CplusPlus)
    Python+=3
    CplusPlus+=1
    if CplusPlus==210:
        break
    Cppsecrets.hideturtle()
turtle.done()