from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)  
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 230)  
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
        
    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()
    
    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()