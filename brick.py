import turtle as tt
import random
color_list = ['red','green','blue', 'yellow','orange', 'purple']



class Brick(tt.Turtle):
    def __init__(self, position):
        super().__init__()
        self.brick = tt.Turtle(shape='square')
        self.brick.color(random.choice(color_list))
        self.brick.penup()
        self.brick.shapesize(1, 6, 6)
        self.brick.goto(position)

    # def pop(self):
    #     self.remove()
