#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

DEG_0 = 4.5
DEG_180 = 15

GPIO.setup(7, GPIO.OUT)

pwm = GPIO.PWM(7, 50)

try:
	pwm.start(0)
	pwm.ChangeDutyCycle(DEG_0)
	raw_input("Press ENTER")
	pwm.ChangeDutyCycle(DEG_180)
	raw_input("Press ENTER")
	pwm.stop()
#except:
#	pass
finally:
	GPIO.cleanup()
