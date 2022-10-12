from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for t_index in range(0,6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[t_index])
    t.goto(x=-230, y=y_pos[t_index])
    all_turtles.append(t)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")

if user_bet:
    race_on = True
    
while race_on:
    for turtle in all_turtles: 
        turtle: Turtle = turtle
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {user_bet} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")
        
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
    
screen.exitonclick()