from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.sety(280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
