import turtle
x1 = 10
x2 = 10
radius = 100
turtle.penup()
turtle.goto(x1, x2)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(x1, x2)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(x1 -70, x2 - radius - 20)
turtle.pendown()


turtle.done()