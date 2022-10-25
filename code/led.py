import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #links led to board
dot.brightness=0.5 #sets brightness to half to prevent blindness

print("Make it pink!") #prints "Make it pink!" to the serial monitor 

while True:
    dot.fill((255, 50, 85)) #makes the led pink