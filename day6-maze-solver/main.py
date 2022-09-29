### IGNORE CODE BELOW ###
def turn_left():
    return
def at_goal():
    return
def right_is_clear():
    return
def move():
    return
def wall_on_right():
    return
def front_is_clear():
    return
### IGNORE CODE ABOVE ###
# Access the game below
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
### COPY AND PASTE CODE BELOW INTO WEBSITE ###
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    elif right_is_clear():
        turn_right()
        move()

