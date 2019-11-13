import turtle
bob = turtle.Turtle()
turtle.colormode(255)
turtle.colormode(255)
bob.speed(0)
bob.pensize(3)
turtle.bgcolor("black")
bob.penup()
bob.goto(100,100)
bob.pendown()

bob.width(10)
bob.speed(0)

    
#bob.shape("pentagon")
bob.color("yellow")
bob.begin_fill()
for times in range(5):
    bob.forward(150)
    bob.right(360/5)
    bob.end_fill()

bob.penup()    
bob.forward(0)
bob.left(108)
bob.pendown()

#bob.shape("pentagon")
bob.color("orange")
bob.begin_fill()
for times in range(5):
    bob.forward(150)
    bob.right(360/5)
    bob.end_fill()

bob.penup()
bob.forward(0)
bob.left(108)
bob.pendown()

#bob.shape("pentagon")
bob.color("red")
bob.begin_fill()
for times in range(5):
    bob.forward(150)
    bob.right(360/5)
    bob.end_fill()

bob.penup()
bob.forward(150)
bob.left(108)
bob.pendown()

#bob.shape("pentagon")
bob.color("orange")
bob.begin_fill()
for times in range(5):
    bob.forward(150)
    bob.right(360/5)
    bob.end_fill()

bob.penup()
bob.forward(245)
bob.left(0)
bob.pendown()

#bob.shape("pentagon")
bob.color("red")
bob.begin_fill()
for times in range(5):
    bob.forward(150)
    bob.right(360/5)
    bob.end_fill()

bob.penup()
bob.forward(0)
bob.left(-108)
bob.goto(-110,-40)
bob.pendown()

#bob.shape("pentagon")
bob.color("yellow")
bob.begin_fill()
for times in range(5):
    bob.forward(150)
    bob.right(360/5)
    bob.end_fill()
