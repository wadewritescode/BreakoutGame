import turtle as tt

movespeed = 40
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Paddle(tt.Turtle):
    def __init__(self):
        self.paddle = tt.Turtle(shape='square')
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.shapesize(1, 6, 6)

        starting_x = self.paddle.xcor()
        starting_y = -350

        self.paddle.goto(starting_x, starting_y)





    def paddle_left(self):
        self.paddle.setheading(LEFT)
        new_x = self.paddle.xcor()
        new_y = self.paddle.ycor()
        self.paddle.goto(new_x, new_y)
        self.paddle.forward(15)

    def paddle_right(self):
        self.paddle.setheading(RIGHT)
        new_x = self.paddle.xcor()
        new_y = self.paddle.ycor()
        self.paddle.goto(new_x, new_y)
        self.paddle.forward(15)
