# Hurdle 3
think(0)
def turn_right():
    for i in range(3):
        turn_left()

def jump_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()
        
# Hurdle 4
think(0)
def turn_right():
    for i in range(3):
        turn_left()

def jump_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()

# Maze
think(0)
def turn_right():
    for i in range(3):
        turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()