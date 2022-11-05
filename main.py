import turtle as tt
import random
import time
import paddle
import brick
import ball



screen = tt.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Breakout - An Atari classic')
screen.tracer(0)


pad = paddle.Paddle()
br_list = []
for num in range(0,15):
    if len(br_list) <= 4:
        br = brick.Brick((300 - (150 * (len(br_list) % 5)),350))
        br_list.append(br)
    elif len(br_list) >4 and len(br_list) <=9:
        br = brick.Brick((300 - (150 * (len(br_list) % 5)),300))
        br_list.append(br)
    else :
        br = brick.Brick((300 - (150 * (len(br_list) % 5)),250))
        br_list.append(br)
ball = ball.Ball()





screen.onkey(pad.paddle_left, "Left")
screen.onkey(pad.paddle_right, "Right")

screen.onkeypress(pad.paddle_left, "Left")
screen.onkeypress(pad.paddle_right, "Right")
screen.onkeyrelease(pad.paddle_left, "Left")
screen.onkeyrelease(pad.paddle_right, "Right")

screen.listen()


game_on = True

while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    if ball.ball.ycor() > 380:
        ball.wall_bounce()

    if ball.ball.xcor() > 380 or ball.ball.xcor() < -380:
        ball.horiz_wall_bounce()

    if ball.ball.distance(pad.paddle.xcor(), pad.paddle.ycor()) < 30 or ball.ball.distance(pad.paddle.xcor() - 30, pad.paddle.ycor()) < 30 or ball.ball.distance(pad.paddle.xcor() + 30, pad.paddle.ycor()) < 30 :
        ball.paddle_hit()
        ball.ball.goto(ball.ball.xcor(), pad.paddle.ycor() + 30)

    for bric in br_list:
        if ball.ball.distance(bric.brick.xcor(), bric.brick.ycor()) < 30 or ball.ball.distance(bric.brick.xcor() + 30, bric.brick.ycor()) < 30 or ball.ball.distance(bric.brick.xcor() - 30, bric.brick.ycor()) < 30:
            ball.wall_bounce()
            bric.brick.ht()
            del br_list[br_list.index(bric)]


    if ball.ball.ycor() < -380 or len(br_list) == 0 :
        game_on = False
        screen.update()




screen.mainloop()