import board
import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


i2c = board.I2C()
temp=AnalogIn(board.A0)

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)