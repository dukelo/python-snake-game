from turtle import Turtle

ORIGINAL_PATH = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90.0
DOWN = 270.0
RIGHT = 0.0
LEFT = 180.0


class Snake:

    def __init__(self):

        self.turtles = []
        self.create_sake()
        self.head = self.turtles[0]

    def create_sake(self):

        for position in ORIGINAL_PATH:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle()
        turtle.color("white")
        turtle.shape("square")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend_snake(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):

        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)

        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
