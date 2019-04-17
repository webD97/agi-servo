#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

DEG_0 = 4.5
DEG_90 = 9
DEG_180 = 15

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
