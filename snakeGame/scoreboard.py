from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.speed("fastest")
        self.color("saddle brown")
        
    def write_scoreboard(self):
        self.write(arg=f"Score = {self.score} ", move=False, align="Center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto(0 ,0)
        self.write(arg="Game Over", move=False, align="Center", font=("Arial", 18, "normal"))