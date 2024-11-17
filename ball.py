from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.03

    def move(self, x_cord, y_cord):
        x = self.xcor() + x_cord
        y = self.ycor() + y_cord
        self.teleport(x,y)

    def y_bounce(self):
        if self.ycor() > 280 or self.ycor() < -280:
            return True
        return False

    def game_over(self):
        if self.xcor() > 380 or self.xcor() <-380:
            self.move_speed = 0.03
            return True
        return False

    def bounce(self, rp, lp):
        if self.xcor() == 330 and self.distance(rp.xcor(),rp.ycor()) < 60 or self.xcor() == -330 and self.distance(lp.xcor(),lp.ycor()) < 60:
            self.move_speed *= 0.9
            return True
        return False