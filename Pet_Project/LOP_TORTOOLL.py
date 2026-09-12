import turtle
t = turtle.Pen()
t.shape("turtle")
t.pencolor("blue")
t.speed("fast")
for x in range(4):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

turtle.done()