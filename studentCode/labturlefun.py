import turtle

turtle.shape("turtle")

def four_square():
    turtle.pendown()
    for i in range(0,4):   
        for n in range(0,4):
            turtle.forward(100)
            turtle.right(90)
        turtle.right(90)
    
four_square()

