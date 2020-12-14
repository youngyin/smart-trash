# -*- coding: utf-8 -*-
from sensor.SG90 import *
from sensor.HCSR04 import *
import RPi.GPIO as GPIO

# Eliminate unnecessary warnings
GPIO.setwarnings(False)

# Specify the pin number to be used.
# Open/close the lid
open_TRIG = 20
open_ECHO = 26
SERVO_PIN = 2
# Get distance data.
fill_TRIG = 20
fill_ECHO = 26

# Are your hands close enough to the trash can?
state_close = False # Save the previous state.
is_close = False # Indicate the current state.

setSERVO(angle_to_percent(0), SERVO_PIN)
while True : 
    try:
        # Distance between user and trash can
        open_distance = getDistance(open_TRIG, open_ECHO)
        is_close = (open_distance <= 30)
        
        # Open the lid when your hand is close to the trash can.
        if (is_close == True and state_close == False) : 
            state_close = is_close
            setSERVO(angle_to_percent(180), SERVO_PIN)
            # Get distance data to the bottom of the trash can.
            fill_distance = getDistance(fill_TRIG, fill_ECHO)
            # Store distance data in an external database.
            print(fill_distance)
        
        # Close the lid when your hand falls out of the trash.
        elif (is_close == False and state_close == True) :
            state_close = is_close
            setSERVO(angle_to_percent(0), SERVO_PIN)
            
        time.sleep(0.1)
        
    except KeyboardInterrupt:
       print ("user stops program")
       break
       
    finally : 
        GPIO.cleanup()