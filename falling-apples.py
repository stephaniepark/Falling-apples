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

score = 0

scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.penup()
scoreboard.color("darkblue")
scoreboard.goto(0, 260)

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
  global score
  # Make the apple fall down
  y = apple.ycor()
  apple.sety(y - 10)

  # If caught by basket:
  if basket.distance(apple) < 35 and apple.ycor() > -240:
    score += 1
    update_scoreboard()
    apple.goto(random.randint(-250, 250), 280)

  # If apple goes off screen, instantly respawn at top
  elif apple.ycor() < -280:
    apple.goto(random.randint(-250, 250), 280)

  # Redraw the screen every frame
  screen.update()

  # Repeat every 25 milliseconds
  screen.ontimer(game_loop, 25)

def update_scoreboard():
  scoreboard.clear()
  scoreboard.write("Score " + str(score), align="center", font=("Arial", 16, "bold"))

screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.update()
game_loop()
update_scoreboard()
turtle.done()