import board
import analogio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


TMP36_PIN = board.A0  # Analog input connected to TMP36 output.
i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)


# Function to simplify the math of reading the temperature.
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


# Create TMP36 analog input.
tmp36 = analogio.AnalogIn(TMP36_PIN)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    print("Temperature: {}C {}F".format(temp_C, temp_F))
    time.sleep(1.0)

    if temp_F > 78:
        lcd.clear()
        lcd.set_cursor_pos (1, 0)
        lcd.print("Too hot!")

    if temp_F < 70:
        lcd.clear()
        lcd.set_cursor_pos (1, 0)
        lcd.print("Too cold!")
