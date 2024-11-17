from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,230)
        self.write(f'''SCORE
  {self.score_l} : {self.score_r}''',font=('arial', 20, 'bold'),align='center')

    def line(self):
        line = Turtle()
        line.color('white')
        line.penup()
        line.goto(0, 250)
        line.setheading(270)
        line.width(4)
        while line.ycor() >= -350:
            line.forward(20)
            line.penup()
            line.forward(20)
            line.pendown()
    def rewrite(self):
        self.clear()
        self.write(f'''SCORE
  {self.score_l} : {self.score_r}''', font=('arial', 20, 'bold'), align='center')