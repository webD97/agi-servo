#!/usr/bin/env python3
import time
import math
#from extras import extramath

from physical.PhysicalServo import PhysicalServo
from physical.LogicalServo import LogicalServo
from physical.RoboArm import RoboArm

from Adafruit_PCA9685 import PCA9685

pwm = PCA9685(0x40)
#pwm.set_pwm(5, 0, 600)

armRotation1 = LogicalServo(PhysicalServo(pwm, 5, 400, 2050))
armRotation2 = LogicalServo(PhysicalServo(pwm, 4, 400, 2050))
armRotation3 = LogicalServo(PhysicalServo(pwm, 3, 400, 2050))
armRotation4 = LogicalServo(PhysicalServo(pwm, 2, 400, 2050))
clawRotation = LogicalServo(PhysicalServo(pwm, 1, 350, 1800))
claw = LogicalServo(PhysicalServo(pwm, 0, 350, 1800))

arm = RoboArm(armRotation1, armRotation2, armRotation3, armRotation4, clawRotation, claw)

def reset():
    armRotation1.setAngle(90)
    armRotation2.setAngle(90)
    time.sleep(1)
    armRotation3.setAngle(90)
    armRotation4.setAngle(90)
    arm.claw.open()
    arm.claw.setRotation(90)
    time.sleep(2)

def pickupL():
    armRotation1.setAngle(180)
    time.sleep(1)
    armRotation2.setAngle(0)
    clawRotation.setAngle(180)
    time.sleep(1)
    armRotation3.setAngle(100)
    armRotation4.setAngle(45)
    time.sleep(1)
    arm.claw.close()
    time.sleep(1)

def pickupR():
    armRotation1.setAngle(0)
    time.sleep(1)
    armRotation2.setAngle(0)
    clawRotation.setAngle(180)
    time.sleep(1)
    armRotation3.setAngle(100)
    armRotation4.setAngle(45)
    time.sleep(1)
    arm.claw.close()
    time.sleep(1)

def slot1():
    pass

def slot2():
    pass

def slot3():
    pass

def slot4():
    pass

def slot5():
    armRotation2.setAngle(65)
    armRotation3.setAngle(127)
    time.sleep(1)
    armRotation1.setAngle(90)
    time.sleep(1)
    armRotation2.setAngle(60)
    armRotation3.setAngle(130)
    time.sleep(1)

def slot6():
    pass

def slot7():
    armRotation2.setAngle(40)
    time.sleep(1)
    armRotation4.setAngle(90)
    time.sleep(1)
    armRotation1.setAngle(90)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
    armRotation2.setAngle(30)
    time.sleep(.5)
    armRotation3.setAngle(110)
    time.sleep(.5)
    armRotation4.setAngle(80)
    time.sleep(.5)

""" Roboter Arm Entrypoint """
def main():
    reset()
    pickupL()
    slot7()
    arm.claw.open()

    # coords = extramath.cat2sph(10.0, 2.0, 0.0)
    # print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
