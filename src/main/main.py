#!/usr/bin/env python3
import time
import math
#from extras import extramath

from physical.PhysicalServo import PhysicalServo
from physical.LogicalServo import LogicalServo
from physical.RoboArm import RoboArm

from Adafruit_PCA9685 import PCA9685


""" Roboter Arm Entrypoint """
def main():
    pwm = PCA9685(0x40)

    # TODO: Calibrate servos
    servo1 = LogicalServo(PhysicalServo(pwm, 0, 150, 600))
    servo2 = LogicalServo(PhysicalServo(pwm, 1, 150, 600))
    servo3 = LogicalServo(PhysicalServo(pwm, 2, 150, 600))
    servo4 = LogicalServo(PhysicalServo(pwm, 3, 150, 600))
    servo5 = LogicalServo(PhysicalServo(pwm, 4, 150, 600))
    servo6 = LogicalServo(PhysicalServo(pwm, 5, 150, 600))

    arm = RoboArm(servo1, servo2, servo3, servo4, servo5, servo6)

    arm.claw.open()
    arm.claw.close()

    servo1.setAngle(0)
    time.sleep(1)
    servo1.setAngle(90)
    time.sleep(1)
    servo1.setAngle(180)
    time.sleep(1)
    servo1.setAngle(90)
    time.sleep(1)
    servo1.setAngle(0)

    # coords = extramath.cat2sph(10.0, 2.0, 0.0)
    # print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
