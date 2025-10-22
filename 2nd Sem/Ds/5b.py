import turtle
import random
import time
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(12):
    t.color(colors[i % len(colors)])
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.right(30)

for i in range(6):
    t.color(random.choice(["cyan", "magenta", "white"]))
    for _ in range(36):
        t.circle(50 + i * 10)
        t.right(10)
    t.right(15)
t.clear()
particles = []
for _ in range(25):
    p = turtle.Turtle()
    p.shape("circle")

    p.color(random.choice(colors))
    p.penup()
    p.speed(0)
    p.shapesize(0.3)
    p.goto(random.randint(-300, 300), random.randint(-250, 250))
    particles.append(p)

screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, 0)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan"]

for _ in range(20):
    pen.color(random.choice(colors))
    pen.clear()
    pen.write("TRISPARK", align="center", font=("Arial", 50, "bold"))
    time.sleep(0.2)
for _ in range(50):
    for p in particles:
        p.color(random.choice(colors))
        x, y = p.position()
        p.goto(x + random.randint(-20, 20), y + random.randint(-20, 20))
    time.sleep(0.05)

for i in range(10, 0, -1):
    pen.color(random.choice(colors))
    pen.clear()
    pen.write("TRISPARK", align="center", font=("Arial", 50 - i, "bold"))
    time.sleep(0.1)
pen.clear()
pen.color("white")
pen.write("Thank You!", align="center", font=("Courier", 40, "bold"))
turtle.done()
