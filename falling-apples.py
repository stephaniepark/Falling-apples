import turtle

screen = turtle.Screen()
screen.title("Catch the Falling Apples!")
screen.bgcolor("skyblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the basket player
basket = turtle.Turtle()
basket.shape("square")
basket.color("saddlebrown")
basket.shapesize(stretch_wid=1, stretch_len=4)  # Stretches into a basket shape
basket.penup()
basket.goto(0, -250)

def move_left():
  x = basket.xcor()
  if x > -250:
    basket.setx(x - 35)
    screen.update()
    
def move_right():
    x = basket.xcor()
    if x < 250:
        basket.setx(x + 35)
        screen.update()

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.update()
turtle.done()