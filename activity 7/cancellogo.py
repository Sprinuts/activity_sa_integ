import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the screen background color
turtle.bgcolor("white")

t.speed(5)

t.color("black")
t.pensize(5)
t.penup()
t.goto(0, -200)
t.fillcolor("blue")
t.pendown()
t.begin_fill()
t.circle(200)
t.end_fill()

t.color("black")
t.pensize(5)
t.penup()
t.goto(-145, 73)
t.left(-120)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.circle(160,extent=180)
t.left(90)
t.forward(320)
t.end_fill()

t.color("black")
t.pensize(5)
t.penup()
t.goto(140, -73)
t.right(-90)
t.fillcolor("white")
t.pendown()
t.begin_fill()
t.circle(-160, extent=-180)
t.left(-90)
t.forward(320)
t.end_fill()

t.hideturtle()

turtle.exitonclick()