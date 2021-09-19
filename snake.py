from turtle import *

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]
        self.head.color("green")

    def create_snake(self):
        for pos in POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for pos in range(len(self.squares) - 1, 0, -1):
            x = self.squares[pos - 1].xcor()
            y = self.squares[pos - 1].ycor()
            self.squares[pos].goto(x, y)
        self.head.forward(20)

    def upward(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def downward(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def leftward(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def rightward(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
