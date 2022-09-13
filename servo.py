# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import board
import pwmio
from adafruit_motor import servo


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency= 100)

# Create a servo object, my_servo.
my_servo = servo = servo.Servo(pwm, min_pulse=500, max_pulse=2600)

while True:
    for angle in range(0, 180, 3):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
    for angle in range(180, 0, -3): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
