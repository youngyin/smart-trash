# -*- coding: utf-8 -*-
from SG90 import *
from HCSR04 import *
import RPi.GPIO as GPIO

# Eliminate unnecessary warnings
GPIO.setwarnings(False)

# Specify the pin number to be used.
TRIG = 20
ECHO = 26
SERVO_PIN = 2

# Are your hands close enough to the trash can?
state_close = False  # Save the previous state.
is_close = False  # Indicate the current state.

setSERVO(angle_to_percent(0), SERVO_PIN)
while True:
    try:
        distance = getDistance(TRIG, ECHO)
        is_close = (distance <= 30)
        print (distance)

        # Open the lid when your hand is close to the trash can.
        if (is_close == True and state_close == False):
            state_close = (distance <= 30)
            setSERVO(angle_to_percent(180), SERVO_PIN)

        # Close the lid when your hand falls out of the trash.
        elif (is_close == False and state_close == True):
            state_close = (distance <= 30)
            setSERVO(angle_to_percent(0), SERVO_PIN)

        time.sleep(1)

    except KeyboardInterrupt:
        print("user stops program")
        break

    finally:
        GPIO.cleanup()