import board 
import pwmio
from analogio import AnalogIn, AnalogOut
from digitalio import DigitalInOut, Direction

motor=AnalogOut(board.A0) 

while True:
    motor.value=0