import board
from digitalio import DigitalInOut, Direction, Pull
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency= 100)
my_servo = servo = servo.Servo(pwm, min_pulse=500, max_pulse=2600)
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
            for angle in range(0, 180, 3):
                 my_servo.angle = angle

    prev_state = cur_state

    cur_state2 = btn2.value
    if cur_state2 != prev_state2:
        if not cur_state2:
            print("BTN2 is up")
        else:
            print("BTN2 is down")
            for angle in range(180, 0, -3):
                my_servo.angle = angle

    prev_state2 = cur_state2