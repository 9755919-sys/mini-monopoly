screen_precision = 0
console_precision = 0
myVariable = 0
current_space_number = 0
dice1 = 0
dice2 = 0
space_to_move = 0
FWD = Event()
LT = Event()
RT = Event()
right_turn = Event()
move_forward = Event()
left_turn = Event()

def roll_dice():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    dice1 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice1))
    brain.screen.next_row()
    dice2 = int(round(urandom.uniform(1, 4), 2))
    brain.screen.print(str("Rolled a:") + str(dice2))
    brain.screen.next_row()
    space_to_move = dice1 + dice2

def move():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
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
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    while True:
        roll_dice()
        move()
        complete_task()
        brain.screen.set_cursor(1, 1)
        wait(3, SECONDS)
        brain.screen.clear_row(4)
        brain.screen.set_cursor(brain.screen.row(), 1)
        wait(5, MSEC)

def complete_task():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    brain.screen.print(str("Landedonspace") + str(current_space_number))
    brain.screen.next_row()
    wait(1, SECONDS)
    if current_space_number == 1:
        # Space = GO
        for repeat_count2 in range(4):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
    elif current_space_number == 4:
        # Space = JAIL
        wait(3, SECONDS)
    elif current_space_number == 7:
        # Space = Free Parking
        wait(5, SECONDS)
    elif current_space_number == 10:
        # Space = Go to Jail
        right_turn.broadcast_and_wait()
        for repeat_count3 in range(3):
            move_forward.broadcast_and_wait()
            wait(5, MSEC)
        left_turn.broadcast_and_wait()
        for repeat_count4 in range(3):
            move_forward.broadcast_and_wait()
            wait(5, MSEC)
        for repeat_count5 in range(2):
            right_turn.broadcast_and_wait()
            wait(5, MSEC)
        current_space_number = 4
        wait(1, SECONDS)
    else:
        # Space = Blue 1 or 2, Green 1 or 2, Yellow 1 or 2, or Red 1 or 2
        right_turn.broadcast_and_wait()
        move_forward.broadcast_and_wait()
        for repeat_count6 in range(2):
            left_turn.broadcast_and_wait()
            wait(5, MSEC)
        move_forward.broadcast_and_wait()
        right_turn.broadcast_and_wait()

def left_turn_callback_0():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    motor_1.spin_for(REVERSE, 220, DEGREES)

def when_started1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    current_space_number = 1
    play_game()

def left_turn_callback_1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    motor_5.spin_for(FORWARD, 220, DEGREES)

def right_turn_callback_0():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 220, DEGREES)

def right_turn_callback_1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    motor_5.spin_for(REVERSE, 220, DEGREES)

def move_forward_callback_0():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
    motor_1.spin_for(FORWARD, 400, DEGREES)

def move_forward_callback_1():
    global myVariable, current_space_number, dice1, dice2, space_to_move, FWD, LT, RT, right_turn, move_forward, left_turn, my_event, screen_precision, console_precision
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