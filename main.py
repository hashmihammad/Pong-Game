from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from controls import setup_controls
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

setup_controls(screen, r_paddle, l_paddle)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

    if scoreboard.l_score >= 5:
        scoreboard.declare_winner("Left Player")
        game_is_on = False

    if scoreboard.r_score >= 5:
        scoreboard.declare_winner("Right Player")
        game_is_on = False

screen.exitonclick()
