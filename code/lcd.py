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

prev_state = btn.value
prev_state2=sw.value
lcd.set_cursor_pos (1, 0)
lcd.print("NUMBA:")
lcd.set_cursor_pos (1, 7)
lcd.print(str(val))

while True:
    cur_state2=sw.value
    if cur_state2 != prev_state2:
        lcd.set_cursor_pos (0,0)
        lcd.print("UP  ")
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
                val+=1
        prev_state=cur_state 
    else:
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
                val-=1
        prev_state=cur_state