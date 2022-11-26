import turtle


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Our project")

worker= turtle.Turtle()
worker.color("white")

for i in range(4):
    worker.forward(200)
    worker.right(90)

worker.left(135)
worker.forward((5000**.5)/2)
worker.right(135)
for i in range(4):
    worker.forward(250)
    worker.right(135)
    worker.forward((5000 ** .5) / 2)
    worker.forward(-(5000 ** .5) / 2)
    worker.left(45)
worker.penup()
worker.right(90)
worker.forward(80)
worker.left(90)
worker.forward(80)
worker.pendown()
worker.color("blue")
worker.right(90)
worker.forward(30)
worker.left(90)
worker.forward(20)
worker.penup()
worker.forward(10)
worker.pendown()
worker.left(90)
worker.forward(30)
worker.right(90)
worker.forward(30)
worker.right(135)
worker.forward(15)
worker.left(90)
worker.forward(30)





wn.exitonclick()
