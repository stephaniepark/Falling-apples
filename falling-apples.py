import turtle

screen = turtle.Screen()
screen.title("Catch the Falling Apples!")
screen.bgcolor("skyblue")
screen.setup(width=600, height=600)

# Create the basket player
basket = turtle.Turtle()
basket.shape("square")
basket.color("saddlebrown")
basket.shapesize(stretch_wid=1, stretch_len=4)  # Stretches into a basket shape
basket.penup()
basket.goto(0, -250)
