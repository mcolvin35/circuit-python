
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

while True:
    print((sonar.distance))
    if sonar.distance>=5:
        blue=simpleio.map_range(sonar.distance, 5, 35, 0, 255)
        red=255-sonar.distance
        green=sonar.distance
        dot.fill((red, green, blue))

