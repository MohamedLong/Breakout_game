from turtle import Turtle


class Targets(Turtle):

    def __init__(self):
        super().__init__()
        self.all_targets = []
        self.hideturtle()

    def create_bricks(self):
        y = 100
        self.shape("square")
        for row in range(2):
            x = -265
            y += 25
            while x < 300:
                new_target = Turtle("square")
                new_target.penup()
                new_target.shapesize(stretch_wid=1, stretch_len=3)
                new_target.color('white')
                new_target.goto(x, y)
                self.all_targets.append(new_target)
                x += 65
