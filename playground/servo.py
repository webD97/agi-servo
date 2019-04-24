#!/usr/bin/env python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
import math
import time

# GPIO.setmode(GPIO.BOARD)

DEG_0 = 4.5
DEG_90 = 9
DEG_180 = 15

def alpha(x, y, l):
    # return 180 + math.degrees(math.atan(float(x) / y) - math.asin(math.sqrt(x * x + y * y) / (2 * l)))
    return math.degrees(math.atan(float(x) / y) - math.asin(math.sqrt(x * x + y * y) / (2 * l)))

def beta(x, y, l):
    return math.degrees(2 * math.asin(math.sqrt(x * x + y * y) / (2 * l)))

def set_servo_pulse(chan, pulse):
        pulse_length = 1000000
        pulse_length = 50
        pulse_length //= 4096
        pulse *= 1000
        pulse //= pulse_length
        pwm.set_pwm(chan, 0, pulse)

x = 10
y = 10
l = 20

# print("Alpha: " + str(alpha(x, y, l)))
# print("Beta: " + str(beta(x, y, l)))

# Hier gehts weiter

pwm = Adafruit_PCA9685.PCA9685(address=0x40)
pwm.set_pwm_freq(50)

while True:
    pwm.set_pwm(0, 0, 150)
    time.sleep(1)
    pwm.set_pwm(0, 0, 600)
    time.sleep(1)
    print("Next")

# Altes Zeug
'''
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

pwm1 = GPIO.PWM(7, 50)
pwm2 = GPIO.PWM(11, 50)

try:
        raw_input("Press ENTER")
    pwm2.start(0)
        pwm1.start(0)   
        pwm2.ChangeDutyCycle(DEG_0)
        pwm1.ChangeDutyCycle(DEG_0)    
    raw_input("Press ENTER")
    pwm2.ChangeDutyCycle(DEG_90)
        pwm1.ChangeDutyCycle(DEG_90)    
        raw_input("Press ENTER")
    pwm2.ChangeDutyCycle(DEG_180)
        pwm1.ChangeDutyCycle(DEG_180)   
    raw_input("Press ENTER")
    pwm2.stop()
        pwm1.stop()
        #raw_input("Press ENTER")
        #pwm1.start(0)
    #pwm1.ChangeDutyCycle(DEG_0)
    #raw_input("Press ENTER")
        #pwm1.ChangeDutyCycle(DEG_90)
        #raw_input("Press ENTER")
    #pwm1.ChangeDutyCycle(DEG_180)
        #raw_input("Press ENTER")
    #pwm1.stop()
except:
    pass
finally:
    GPIO.cleanup()
'''
