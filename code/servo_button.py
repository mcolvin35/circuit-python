import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency= 100)
my_servo = servo = servo.Servo(pwm, min_pulse=500, max_pulse=2600)
btn1 = DigitalInOut(board.D13) #links button 1 to board
btn2 = DigitalInOut(board.D12) #links button 2 to board
btn1.direction = Direction.INPUT #btn1 is input 
btn1.pull = Pull.UP #recognize input when button is released
btn2.direction = Direction.INPUT 
btn2.pull = Pull.UP

prev_state = btn1.value #previous state is btn1 
prev_state2 = btn2.value
while True:
    cur_state = btn1.value #current state is btn1 
    if cur_state != prev_state: #if cur_state is different than prev_state
        if not cur_state:
            print("BTN1 is up")
        else:
            print("BTN1 is down")
            for angle in range(0, 180, 3):
                 my_servo.angle = angle #servo moves 180 degrees in one direction 

    prev_state = cur_state #sets prev_state to cur_state 

    cur_state2 = btn2.value
    if cur_state2 != prev_state2:
        if not cur_state2:
            print("BTN2 is up")
        else:
            print("BTN2 is down")
            for angle in range(180, 0, -3):
                my_servo.angle = angle #servo moves 180 degrees in other direction 

    prev_state2 = cur_state2