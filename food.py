from turtle import *
import random
import snake

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(.5, .5)
        self.penup()
        self.speed("fastest")
        self.next_food()

    def next_food(self):
        x = random.randint(0, 260)
        y = random.randint(0, 260)
        self.goto(x, y)

