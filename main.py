import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Interactive Turtle In Python")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(60)

def rotate_angel_right():
    turtle_instance.setheading(turtle_instance.heading()-20)
 #   turtle_instance.right(10)

def rotate_angel_left():
    turtle_instance.setheading(turtle_instance.heading()+20)
  #  turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(turtle_forward,"space")
drawing_board.onkey(rotate_angel_left,"Up")
drawing_board.onkey(rotate_angel_right,"Down")
drawing_board.onkey(clear_screen,"c")
drawing_board.onkey(turtle_return_home,"h")
drawing_board.onkey(turtle_pen_up,"q")
drawing_board.onkey(turtle_pen_down,"w")






turtle.mainloop()