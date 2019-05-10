#!/usr/bin/env python3

import math
from extras import extramath

from physical.PhysicalServo import PhysicalServo
from physical.LogicalServo import LogicalServo
from physical.RoboArm import RoboArm

""" Roboter Arm Entrypoint """
def main():
    servo1 = LogicalServo(PhysicalServo(0, 0, 0, 0))
    servo2 = LogicalServo(PhysicalServo(0, 0, 0, 0))
    servo3 = LogicalServo(PhysicalServo(0, 0, 0, 0))
    servo4 = LogicalServo(PhysicalServo(0, 0, 0, 0))

    arm = RoboArm(servo1, servo2, servo3, servo4)

    arm.openClaw()
    arm.moveTo(1, 2, 3)
    arm.closeClaw()
    arm.moveTo(3, 4, 5)
    arm.openClaw()

    coords = extramath.cat2sph(1.0, 0.0, 0.0)
    print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
