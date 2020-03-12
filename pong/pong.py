# Simple Pong in Python 3 for Beginners
# FCC

import turtle
# import os

# create window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0) #window won't update- speeds up game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # max possible speed
paddle_a.shape("square")
paddle_a.color("pink")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # no line when it moves
paddle_a.goto(-350, 0) # position it starts at

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # max possible speed
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # no line when it moves
paddle_b.goto(350, 0) # position it starts at

# Ball
ball = turtle.Turtle()
ball.speed(0) # max possible speed
ball.shape("square")
ball.color("pink")
ball.penup() # no line when it moves
ball.goto(0, 0) # position it starts at
ball.dx = 2 # every time the ball moves, it moves by 2 px
ball.dy = 2

# Pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle() # don't want to see turtle, just text
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "k")

# os.system("afplay fuel.wav&") # sort of annoying, probably you don't want this

# Main game loop
while True:
    wn.update() # updates screen every time loop runs
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 70 and ball.ycor() > paddle_b.ycor() - 70):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 70 and ball.ycor() > paddle_a.ycor() - 70):
        ball.setx(-340)
        ball.dx *= -1
