screen_precision = 0
console_precision = 0
FWD = Event()
LT = Event()
RT = Event()
right_turn = Event()
move_forward = Event()
left_turn = Event()
myVariable = 0
current_space_number = 0
dice1 = 0
dice2 = 0
space_to_move = 0
properties_visited = 0
RED1 = 0
RED2 = 0
BLUE1 = 0
BLUE2 = 0
GREEN1 = 0
GREEN2 = 0
YELLOW1 = 0
YELLOW2 = 0

def roll_dice():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    space_to_move = dice1 + dice2

def move():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    brain.screen.print(str(space_to_move) + str("spaces!"))
    brain.screen.next_row()
    for repeat_count in range(int(space_to_move)):
        move_forward.broadcast_and_wait()
        current_space_number = current_space_number + 1
        if current_space_number > 12:
            current_space_number = 1
        if current_space_number == 1:
            right_turn.broadcast_and_wait()
        if current_space_number == 4:
            right_turn.broadcast_and_wait()
        if current_space_number == 7:
            right_turn.broadcast_and_wait()
        if current_space_number == 10:
            right_turn.broadcast_and_wait()
        wait(5, MSEC)

def play_game():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    while not properties_visited == 8:
        roll_dice()
        move()
        complete_task()
        brain.screen.set_cursor(1, 1)
        wait(3, SECONDS)
        brain.screen.clear_row(4)
        brain.screen.set_cursor(brain.screen.row(), 1)
        wait(5, MSEC)

def complete_task():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    brain.screen.print(str("Landedonspace") + str(current_space_number))
    brain.screen.next_row()
    wait(1, SECONDS)

def when_started1():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    current_space_number = 1
    BLUE1 = "false"
    BLUE2 = "false"
    GREEN1 = "false"
    GREEN2 = "false"
    RED1 = "false"
    RED2 = "false"
    YELLOW1 = "false"
    YELLOW2 = "false"
    play_game()

def left_turn_callback_0():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    motor_1.spin_for(REVERSE, 220, DEGREES)

def left_turn_callback_1():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 220, DEGREES)

def right_turn_callback_0():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 220, DEGREES)

def right_turn_callback_1():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    motor_5.spin_for(REVERSE, 220, DEGREES)

def move_forward_callback_0():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 400, DEGREES)

def move_forward_callback_1():
    global FWD, LT, RT, right_turn, move_forward, left_turn, my_event, myVariable, current_space_number, dice1, dice2, space_to_move, properties_visited, RED1, RED2, BLUE1, BLUE2, GREEN1, GREEN2, YELLOW1, YELLOW2, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 400, DEGREES)

# system event handlers
left_turn(left_turn_callback_0)
left_turn(left_turn_callback_1)
right_turn(right_turn_callback_0)
right_turn(right_turn_callback_1)
move_forward(move_forward_callback_0)
move_forward(move_forward_callback_1)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

when_started1()
