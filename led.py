import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it pink!")

while True:
    dot.fill((255, 50, 85))