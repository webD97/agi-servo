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
    servo5 = LogicalServo(PhysicalServo(0, 0, 0, 0))
    servo6 = LogicalServo(PhysicalServo(0, 0, 0, 0))

    arm = RoboArm(servo1, servo2, servo3, servo4, servo5, servo6)

    arm.claw.open()
    arm.claw.close()

    # coords = extramath.cat2sph(10.0, 2.0, 0.0)
    # print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
