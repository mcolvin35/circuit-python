import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull

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