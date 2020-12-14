# -*- coding: utf-8 -*-
# https://m.blog.naver.com/roboholic84/220319850312
import RPi.GPIO as GPIO
import time

def getDistance(TRIG, ECHO) :
    # GPIO pin number mode setting 
    GPIO.setmode(GPIO.BCM)
    
    # Servo pin output/input setting
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(0.5)
    
    GPIO.output(TRIG, True)
    time.sleep(0.001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO) == 0 : 
        pulse_start = time.time()
    
    while GPIO.input(ECHO) == 1 : 
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    return distance  
    
if __name__ =="__main__" :
    # After attaching the distance sensor, 
    # check if it works.
    TRIG = 20
    ECHO = 26
    for i in range(10) : 
        distance = getDistance(TRIG, ECHO)
        print(distance, "cm")
        time.sleep(1)