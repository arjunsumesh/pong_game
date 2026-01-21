from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)   #To turn the animation off and update it inside the while loop to see the paddle

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)   #Making the while loop sleep for 0.1 seconds for the ball to move slowly
    screen.update()
    ball.move()

    # Detecting collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        # Ball should bounce
        ball.bounce_y()
    #Detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #Detect r_paddle misses
    if ball.xcor()>380:
        ball.reset_position()
    #Detect l_paddle misses
    if ball.xcor()<-380:
        ball.reset_position()



screen.exitonclick()
