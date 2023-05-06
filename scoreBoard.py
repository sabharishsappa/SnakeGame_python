from turtle import Turtle

ALIGNMENT = "center"
FONT ="Arial", 24, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score =0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0,260)

        self.updateScoreBoard()

    def updateScoreBoard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=(FONT))

    def foodCollision(self):
        self.score+=1
        self.clear()
        self.updateScoreBoard()

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=(FONT))
