import turtle
import random

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

# Create the apple
apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(random.randint(-250, 250), 280)

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

def game_loop():
  # Make the apple fall down
  y = apple.ycor()
  apple.sety(y - 10)

  # If apple goes off screen, instantly respawn at top
  if apple.ycor() < -280:
    apple.goto(random.randint(-250, 250), 280)

  # Redraw the screen every frame
  screen.update()

  # Repeat every 25 milliseconds
  screen.ontimer(game_loop, 25)

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.update()
game_loop()
turtle.done()