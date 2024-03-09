import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the screen background color
turtle.bgcolor("white")

# Set the turtle's speed
t.speed(2)

# Draw a circle
t.color("red")
t.goto(0, -100)
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw a diamond inside the circle
t.color("black")
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
for _ in range(2):
    t.left(45)
    t.forward(140)
    t.left(90)
    t.forward(140)
    t.left(45)
t.end_fill()


# Draw a square inside the diamond
t.color("blue")
t.penup()
t.goto(-50, 50)
t.pendown()
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()

t.hideturtle()

turtle.exitonclick()