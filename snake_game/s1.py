import turtle
import random
import time

screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

# Creating border
turtle.speed(5)
turtle.pensize()
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Score
score = 0
delay = 0.1
scores = turtle.Screen()
scores.title("scores")

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("indigo")
snake.penup()
snake.goto(8, 8)
snake.direction = "stop"

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(38, 38)
old_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(8, 388)
scoring.write("score: ", align="center", font=("courier", 24, "bold"))

# Reset button
reset_button = turtle.Turtle()
reset_button.speed(0)
reset_button.shape("square")
reset_button.color("green")
reset_button.penup()
reset_button.goto(-200, -300)
reset_button.hideturtle()
reset_button.write("Reset", align="center", font=("courier", 24, "bold"))

# Define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Key binding
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Reset function
def reset_game(x, y):
    global score, delay, old_fruit
    score = 0
    delay = 0.1
    scoring.clear()
    scoring.write("score:{}".format(score), align="center", font=("courier", 24, "bold"))
    snake.goto(8, 8)
    snake.direction = "stop"
    for segment in old_fruit:
        segment.goto(1000, 1000)
    old_fruit.clear()
    reset_button.hideturtle()  # Hide the reset button again

# Click binding for reset button
reset_button.onclick(reset_game)

# Main loop
while True:
    screen.update()

    # Snake and fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-298, 278)
        y = random.randint(-248, 248)
        fruit.goto(x, y)
        scoring.clear()
        score += 1
        scoring.write("score:{}".format(score), align="center", font=("courier", 24, "bold"))
        delay -= 0.001
        # Creating new food
        new_fruit = turtle.Turtle()
        new_fruit.speed(8)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Adding balls to snake
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    move()

    # Snake and border collision
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("Game over\nYour score is {}".format(score), align="center", font=("courier", 30, "bold"))
        reset_button.showturtle()  # Show the reset button
        break

    # Snake collision
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("Game over\nYour score is {}".format(score), align="center", font=("courier", 30, "bold"))
            reset_button.showturtle()  # Show the reset button
            break

    time.sleep(delay)

turtle.done()
