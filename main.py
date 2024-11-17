from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()
score.line()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_on = True

x_cord = 5
y_cord = 5

while game_on:
    ball.move(x_cord, y_cord)
    if ball.y_bounce():
        y_cord = -y_cord
    if ball.bounce(r_paddle, l_paddle):
        x_cord = -x_cord
    if ball.game_over():
        if ball.xcor() > 380:
            score.score_l += 1
        elif ball.xcor() < -380:
            score.score_r += 1
        score.rewrite()
        ball.home()
        x_cord = -x_cord
        y_cord = -y_cord
        r_paddle.goto(350,0)
        l_paddle.goto(-350,0)
    screen.update()
    sleep(ball.move_speed)




screen.exitonclick()