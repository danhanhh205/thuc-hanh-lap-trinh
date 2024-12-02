print ("Nguyễn Danh Ánh")
print ("235752021610023")

import turtle
import random

colors = ["red", "green", "blue"]

painter = turtle.Turtle()

for layer in range(3):
    for i in range(10):
        color = random.choice(colors)
        painter.pencolor(color)
        painter.circle(100)
        painter.right(30)
        painter.left(60)
    painter.penup()
    painter.forward(20)
    painter.pendown()

turtle.done()
