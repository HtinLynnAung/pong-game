# This Pong game tutorial is coded by HtinLinAung(LeoKrypto)
# Date: 5.10.2024

import turtle as t
import winsound

playerA_score = 0
playerB_score = 0
paused = False  # Initially the game is not paused

# create a window and declare a variable called window and call the screen()
window = t.Screen()
window.title('The Pong Game')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
leftPaddle = t.Turtle()
leftPaddle.speed(30)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=0.5)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# Creating the right paddle
rightPaddle = t.Turtle()
rightPaddle.speed(30)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=0.5)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# Creating the ball
ball = t.Turtle()
ball.speed(30)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball_x_direction = 0.2
ball_y_direction = 0.2

# Pause text display turtle
pause_turtle = t.Turtle()
pause_turtle.speed(0)
pause_turtle.color("white")
pause_turtle.penup()
pause_turtle.hideturtle()
pause_turtle.goto(0, 0)

# Function to pause the game
def toggle_pause():
    global paused
    paused = not paused  # Toggle the paused state

    if paused:
        pause_turtle.clear()  # clear any previous message
        pause_turtle.write("PAUSE", align="center", font=('Arial', 36, "normal"))
    else:
        pause_turtle.clear()  # Remove "pause" message when resuming


# Creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score", align="center", font=('Arial', 24, 'normal'))


# Creating the movement of leftpaddle
def leftpaddle_up():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)


def leftpaddle_down():
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)


# Creating the movement of rightpaddle
def rightpaddle_up():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)


def rightpaddle_down():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)


# Assign keys to paly
window.listen()
window.onkeypress(leftpaddle_up, 'w')
window.onkeypress(leftpaddle_down, 's')
window.onkeypress(rightpaddle_up, 'Up')
window.onkeypress(rightpaddle_down, 'Down')
window.onkeypress(toggle_pause, 'space')

while True:
    window.update()

    if not paused:
        # moving the ball
        ball.setx(ball.xcor() + ball_x_direction)
        ball.sety(ball.ycor() + ball_y_direction)

        # border set up
        if ball.ycor() > 290:
            ball.sety(290)
            ball_y_direction *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball_y_direction *= -1

        # Right width paddle border
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_x_direction *= -1
            playerA_score = playerA_score + 1
            pen.clear()
            pen.write("Player A: {}     Player B: {}".format(playerA_score, playerB_score), align="center", font=('Monaco', 24, "normal"))
            winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)

        # left width paddle border
        if (ball.xcor()) < -390:
            ball.goto(0, 0)
            ball_x_direction *= -1
            playerB_score = playerB_score + 1
            pen.clear()
            pen.write("Player A: {}     Player B: {}".format(playerA_score, playerB_score), align="center", font=('Monaco', 24, "normal"))
            winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)

        # Handling the collisions with paddles.
        if (ball_x_direction > 0 and ball.xcor() > 340 and ball.xcor() < 350 and
                ball.ycor() < rightPaddle.ycor() + 50 and ball.ycor() > rightPaddle.ycor() - 50):
            ball.setx(340)
            ball_x_direction *= -1
            winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)

        if (ball_x_direction < 0 and ball.xcor() < -340 and ball.xcor() > -350 and
                ball.ycor() < leftPaddle.ycor() + 50 and ball.ycor() > leftPaddle.ycor() - 50):
            ball.setx(-340)
            ball_x_direction *= -1
            winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)









