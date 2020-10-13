import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(360):
    for colours in ['red','blue','cyan','green','yellow','white']:
        turtle.color(colours)
        turtle.circle(360)
        turtle.right(10)
turtle.hideturtle()