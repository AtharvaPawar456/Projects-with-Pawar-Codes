import turtle as tut
Pawar = tut.Screen()
Pawar.title("Animation Circle ")
turt=tut.Turtle()
tut.bgcolor("black")
turt.speed(9)
turt.pensize(5)
n=10
i=10
a=10
b=10
while n <= 60:
    turt.color("red")
    turt.circle(n)
    n = n+10
while i <= 60:
    turt.color("blue")
    turt.circle(i)
    i = i+10
while a <= 60:
    turt.color("green")
    turt.circle(a)
    a = a+10
while b <= 60:
    turt.color("yellow")
    turt.circle(b)
    b = b+10
tut.done()