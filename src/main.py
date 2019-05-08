#!/usr/bin/env python3

import math
from extras import extramath

"""
Roboter Arm Entrypoint
"""
def main():
    coords = extramath.cat2sph(1.0, 0.0, 0.0)
    print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
