import board 
from analogio import AnalogIn, AnalogOut

mot=AnalogOut(board.A1) #sets motor as output and links it to A1
pot=AnalogIn(board.A0) #sets potentiometer as input and links it to A0 (true analog)

while True:
    print(pot.value) #prints potentiometer value to the serial monitor                                                                                                                                                                                                       
    mot.value=(pot.value) #sets the speed of the motor to the value of the potentiometer
