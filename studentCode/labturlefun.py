import turtle

turtle.shape("turtle")
turtle.screensize(canvwidth=720, canvheight=720)

def four_square():
    turtle.pendown()
    for i in range(0, 4):   
        for n in range(0,4):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(90)
    
def empty_plane():
    turtle.speed('fast')
    turtle.seth(0)
    for i in range(0, 4):
        for n in range(0, 10):
            turtle.pendown()
            turtle.forward(10)
            turtle.right(90)
            if n % 5 == 0:
                turtle.forward(5)
                turtle.right(180)
                turtle.forward(10)
                turtle.right(180)
                turtle.forward(5)    
            else:
                turtle.forward(2)
                turtle.right(180)
                turtle.forward(4)
                turtle.right(180)
                turtle.forward(2)
            turtle.right(270)
        turtle.penup()
        turtle.right(180)
        turtle.forward(100)
        turtle.right(270)
    turtle.speed('normal')
        
def single_triangle():
    turtle.pendown()
    turtle.right(60)
    for i in range(0, 3):
        turtle.forward(100)
        turtle.right(120)

def touching_triangles():
    turtle.seth(0)
    single_triangle()
    turtle.right(120)
    single_triangle()


turtle.penup()
turtle.goto(0, 200)
four_square()
turtle.penup()
turtle.goto(200, 0)
empty_plane()
turtle.penup()
turtle.goto(0, -200)
single_triangle()
turtle.penup()
turtle.goto(-200, 0)
touching_triangles()
