from turtle import Turtle

position = [(0, 0), (-20, 0), (-40,0)]

UP = 90
DOWN =270
LEFT = 180
RIGHT=0


class Snake():
    def __init__(self):
        self.bodyparts = []
        self.create_snake()
        self.head = self.bodyparts[0]

    def create_snake(self):
        for pos in position:
           self.add_body(pos)

    def add_body(self, pos):
            body = Turtle("square")
            body.penup()
            body.color("sea green")
            body.goto(pos)
            self.bodyparts.append(body)

    def extend(self):
        self.add_body(self.bodyparts[-1].position())


    def move(self):
        for i in range(len(self.bodyparts)-1, 0, -1):
            x = self.bodyparts[i - 1].xcor()
            y = self.bodyparts[i - 1].ycor()
            self.bodyparts[i].goto(x, y)
    
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)