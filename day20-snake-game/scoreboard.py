from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)    
        self.hideturtle()
        self.update_scoreboard()
        
    def get_highscore(self):
        with open("highscore.txt", 'r') as file:
            return int(file.read())
        
    def set_highscore(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.set_highscore()
        self.score =  0
        self.update_scoreboard()
        
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()