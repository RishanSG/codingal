import turtle
t=turtle.Turtle()

t.pensize(3)
t.speed(3)

colorlist=["red","blue","green","purple"]

for i in range (4):
    t.color(colorlist[i%4])
    t.forward(100)
    t.left(90)