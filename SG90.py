#-*-coding:utf-8-*- 
import RPi.GPIO as GPIO
import time

# Set function to calculate percent from angle
# https://raspberry-pi.kr/%EC%84%9C%EB%B3%B4-%EB%9D%BC%EC%A6%88%EB%B2%A0%EB%A6%AC-%ED%8C%8C%EC%9D%B4/
def angle_to_percent (angle) :
    if angle > 180 or angle < 0 :
        return False

    start = 2.5
    end = 12.5
    ratio = (end - start)/180 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio
    return start + angle_as_percent
    
def setSERVO(DutyCycle, SERVO_PIN) :    
    # GPIO pin number mode setting
    GPIO.setmode(GPIO.BCM)

    # Servo pin output setting
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    # Create a PWM instance servo and set the frequency to 50.
    servo = GPIO.PWM(SERVO_PIN,50)
    
    # Start with PWM duty ratio 0
    servo.start(0)
    
    # Move the servo motor as much as you want by changing the duty ratio.
    servo.ChangeDutyCycle(DutyCycle)
    time.sleep(1)
    
    # Reset settings
    servo.stop()
    GPIO.cleanup()
    
if __name__ =="__main__" :
    # After connecting the motor to the trash can, 
    # adjust so that the trash can is closed at 0 degrees.
    SERVO_PIN = 2
    setSERVO(angle_to_percent(0), SERVO_PIN)
    if (input("Are the lid properly closed? (Y/N)")=="Y") : 
        # Test opening and closing the trash can.
        for i in range(3) : 
            setSERVO(angle_to_percent(180), SERVO_PIN)
            setSERVO(angle_to_percent(0), SERVO_PIN)