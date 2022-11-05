import turtle as tt

class Ball(tt.Turtle):

    def __init__(self):
        super().__init__()
        self.ball = tt.Turtle()
        self.ball.penup()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.resizemode("user")
        self.beginning_time = 0.1
        self.ball.x_move_value = 5
        self.ball.y_move_value = 5


    def move(self):
        self.ball.x_cur = self.ball.xcor()
        self.ball.y_cur = self.ball.ycor()
        self.ball.goto(self.ball.x_cur + self.ball.x_move_value, self.ball.y_cur + self.ball.y_move_value)

    def wall_bounce(self):
        if self.ball.y_move_value > 0:
            self.ball.y_move_value = -abs(self.ball.y_move_value)
        elif self.ball.y_move_value < 0:
            self.ball.y_move_value = abs(self.ball.y_move_value)


    def horiz_wall_bounce(self):
        if self.ball.x_move_value > 0:
            self.ball.x_move_value = -abs(self.ball.x_move_value)
        elif self.ball.x_move_value < 0:
            self.ball.x_move_value = abs(self.ball.x_move_value)


    def paddle_hit(self):
        if self.ball.y_move_value > 0:
            self.ball.y_move_value = -abs(self.ball.y_move_value)
        elif self.ball.y_move_value < 0:
            self.ball.y_move_value = abs(self.ball.y_move_value)