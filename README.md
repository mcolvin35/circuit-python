# **Engineering Notebook Code**
## ***Table of Contents***
* [Hello Circuitpython](#Hello-Circuitpython!)
* [Servo](#Servo)
* [Ultrasonic Sensor](#ultrasonic-sensor)
* [LCD](#lcd)


## ***Hello Circuitpython!***
### **Description**
Get **Circuitpython** and the **Metroexpress** boards up and running, make the onboard neopixel LED **glow**
### **Evidence** 
```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #links led to board
dot.brightness=0.5 #sets brightness to half to prevent blindness

print("Make it pink!") #prints "Make it pink!" to the serial monitor 

while True:
    dot.fill((255, 50, 85)) #makes the led pink
```

### **Image**
### **Reflection**
Getting everything set up was overwhelming and complicated, but Mr. H, River, and Josie were super helpful in getting things working. Thanks!


## ***Servo***
### **Description**
Control a **180° servo** with buttons
### **Evidence**
```python

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
```
### **Image**
### **Reflection**
For this assignment I finally learned how button debouncing actually works, it checks for the actual change in value rather than when the value is 1 or 0 so that you don't get repeat detections!

## ***Ultrasonic Sensor***
### **Description**
Get the neopixel LED to shift through the **color spectrum** based on **distance** detected by an ultrasonic sensor 
### **Evidence**
```python
import time
import board
import adafruit_hcsr04
import simpleio 
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6) #links sensor to pins and creates variable
dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #links neopixel to board and sets variable 
dot.brightness = 0.5 #sets led brightness to half so i don't go blind 

while True:
    try:
        cm=sonar.distance #sets sonar distance to a new variable to avoid issues 

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

    print((cm,)) #prints cm to serial monitor 
    if cm<5: #if cm is less than 5 
        dot.fill((255, 0, 0)) #led is full red 
    if cm>=5 and cm<20:
        x=simpleio.map_range(cm, 5, 20, 0, 255) #maps cm to a value usable by the led 
        red=255-x
        green=0
        blue=x
        dot.fill((red, green, blue)) #red goes down as cm goes up and blue goes up with cm 
    if cm>=20 and cm<35: #if cm is in between 20 and 35
        y=simpleio.map_range(cm, 20, 35, 0, 255) #maps cm to a value usable by the led
        red=0
        green=y
        blue=255-y
        dot.fill((red, green, blue)) #blue goes down as cm goes up and green goes up with cm
    if cm>35: #if cm is more than 35
        dot.fill((0, 255, 0)) #led is full green
```
### **Image**
<img src="https://github.com/mcolvin35/circuit-python/blob/master/images/ultrasonic_led.gif?raw=true" width="500">

### **Reflection**
This assignment was really fun for me and it felt like I really got into a flow with understanding and being able to explain my code well enough for others to learn from me. [This spreadsheet was also super helpful for figuring out how to do the math!](https://docs.google.com/spreadsheets/d/e/2PACX-1vRzoIejkQqugrDoWHBw14qTI0HifXba92WiyQ24whEnzWcCUaCDYu6ifMQKK5O5Ilkxrd7UKIxPLBCW/pubhtml)

## ***LCD***
### **Description**
Get an LCD screen to count up when a button is pressed when switch is **up**, and down when the switch is **down**
### **Evidence**
```python
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull\

i2c = board.I2C()
btn=DigitalInOut(board.D12) #links btn to board
sw=DigitalInOut(board.D13) #links switch to board 
sw.direction=Direction.INPUT
btn.direction=Direction.INPUT #btn and switch are inputs 
btn.pull=Pull.DOWN

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
toggle=sw.value #toggle variable is switch value 
val=0

prev_state = btn.value #debouncing 
prev_state2=sw.value
lcd.set_cursor_pos (1, 0) #sets cursor to given coordinates on lcd screen
lcd.print("NUMBA:") #print "NUMBA:" on lcd screen
lcd.set_cursor_pos (1, 7) #sets the cursor behind "NUMBA:"
lcd.print(str(val)) #prints the variable, which is 0 right now 

while True:
    cur_state2=sw.value
    if cur_state2 != prev_state2: #when switch is up
        lcd.set_cursor_pos (0,0)
        lcd.print("UP  ") #prints "UP  " in the top left, the double space clears any previous values 
        cur_state = btn.value #debouncing
        if cur_state != prev_state:
            if not cur_state: #if button is not pressed 
                lcd.clear() #clears the lcd screen
                lcd.set_cursor_pos (1, 0)
                lcd.print("NUMBA:") 
                lcd.set_cursor_pos (1, 7)
                lcd.print(str(val))
            else: #if button is pressed 
                lcd.clear()
                lcd.set_cursor_pos (1, 0)
                lcd.print("NUMBA:")
                lcd.set_cursor_pos (1, 7)
                lcd.print(str(val))
                val+=1 #value goes up by 1
        prev_state=cur_state #debouncing 
    else: #when switch is down 
        lcd.set_cursor_pos (0,0)
        lcd.print("DOWN") 
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                lcd.clear()
                lcd.set_cursor_pos (1, 0)
                lcd.print("NUMBA:")
                lcd.set_cursor_pos (1, 7)
                lcd.print(str(val))
            else:
                lcd.clear()
                lcd.set_cursor_pos (1, 0)
                lcd.print("NUMBA:")
                lcd.set_cursor_pos (1, 7)
                lcd.print(str(val))
                val-=1 #value goes down by 1 
        prev_state=cur_state
```
### **Image**
<img src="https://github.com/mcolvin35/circuit-python/blob/master/images/lcd.gif?raw=true" width="500">

### **Reflection**
It was pretty tricky figuring out how to get the LCD to print a variable, but I eventually got it with some help. Getting the LCD connected to the board was also pretty tough. 
