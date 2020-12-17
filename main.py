# -*- coding: utf-8 -*-
from SG90 import *
from HCSR04 import *
from updateDB import *
import RPi.GPIO as GPIO

# Eliminate unnecessary warnings
GPIO.setwarnings(False)

# Specify the pin number to be used.
# Open/close the lid
open_TRIG = 20
open_ECHO = 26
SERVO_PIN = 2
# Get distance data.
fill_TRIG = 27
fill_ECHO = 17

# Are your hands close enough to the trash can?
state_close = False # Save the previous state.
is_close = False # Indicate the current state.

setSERVO(angle_to_percent(0), SERVO_PIN)

try : 
    bottom_distance = int(getBottomDistance())
    if bottom_distance<5 : 
        bottom_distance = max([getDistance(fill_TRIG, fill_ECHO) for i in range(3)])

except : 
    bottom_distance = max([getDistance(fill_TRIG, fill_ECHO) for i in range(3)])
    setBottomDistance(bottom_distance)

bottom_distance = 18.5
print("bottom_distance: ", bottom_distance)

while True : 
    try:
        # Distance between user and trash can
        open_distance = getDistance(open_TRIG, open_ECHO)
        is_close = (open_distance <= 30)
        
        # Open the lid when your hand is close to the trash can.
        if (is_close == True and state_close == False) : 
            state_close = is_close
            setSERVO(angle_to_percent(180), SERVO_PIN)
        
        # Close the lid when your hand falls out of the trash.
        elif (is_close == False and state_close == True) :
            state_close = is_close
            setSERVO(angle_to_percent(0), SERVO_PIN)
            # Get distance data to the bottom of the trash can.
            fill_distance = max([getDistance(fill_TRIG, fill_ECHO) for i in range(3)])
            # Store distance data in an external database.
            pushData(fill_distance, bottom_distance)
            
        time.sleep(0.1)
        
    except KeyboardInterrupt:
       print ("user stops program")
       break
       
    finally : 
        GPIO.cleanup()