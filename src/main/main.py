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

    pwm.set_pwm(5, 0, 600)

    # TODO: Calibrate servos
    armRotatation1 = LogicalServo(PhysicalServo(pwm, 5, 400, 2050))
    armRotation2 = LogicalServo(PhysicalServo(pwm, 4, 400, 2050))
    armRotation3 = LogicalServo(PhysicalServo(pwm, 3, 400, 2050))
    armRotation4 = LogicalServo(PhysicalServo(pwm, 2, 400, 2050))
    clawRotation = LogicalServo(PhysicalServo(pwm, 1, 350, 1800))
    claw = LogicalServo(PhysicalServo(pwm, 0, 350, 1800))

    arm = RoboArm(armRotatation1, armRotation2, armRotation3, armRotation4, clawRotation, claw)

    arm.claw.open()
    arm.claw.close()

    armRotatation1.setAngle(0)
    time.sleep(1)

    armRotatation1.setAngle(90)
    time.sleep(1)

    armRotatation1.setAngle(180)
    time.sleep(1)

    armRotatation1.setAngle(90)
    time.sleep(1)

    armRotatation1.setAngle(0)

    # coords = extramath.cat2sph(10.0, 2.0, 0.0)
    # print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
