import turtle as tut
tut.bgcolor("black")
Pawar = tut.Screen()
Pawar.title("Animation Circle ")
turtle=tut.Turtle()
turtle.color("red")
turtle.speed(0)
turtle.hideturtle()
for i in range(100):
    turtle.circle(i*2)
    turtle._rotate(5)

tut.done()