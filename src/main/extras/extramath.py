from collections import namedtuple
import math

SphereCoords = namedtuple("SphereCoords", ["radius", "inclination", "azimuth"])


def cat2sph(x: float, y: float, z: float) -> SphereCoords:
    """ Converts cartesian coordinates (x, y, z) to spherical coordinates
    (radius, inclination, azimuth)

            Parameters:
            x (float): The x part of the coordinate
            y (float): The y part of the coordinate
            z (float): The z part of the coordinate

            Returns:
            SphereCoords: The equivalent spherical coordinates
    """
    r: float = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    inclination: float = math.acos(z / r)
    azimuth: float = math.atan2(y, x)

    return SphereCoords(r, inclination, azimuth)
