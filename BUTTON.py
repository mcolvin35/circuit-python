import board
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D13)
btn2 = DigitalInOut(board.D12)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

prev_state = btn1.value
prev_state2 = btn2.value
while True:
    cur_state = btn1.value
    if cur_state != prev_state:
        if not cur_state:
            print("BTN1 is up")
        else:
            print("BTN1 is down")

    prev_state = cur_state

    cur_state2 = btn2.value
    if cur_state2 != prev_state2:
        if not cur_state2:
            print("BTN2 is up")
        else:
            print("BTN2 is down")

    prev_state2 = cur_state2