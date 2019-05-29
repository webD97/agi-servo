from .PhysicalServo import PhysicalServo

class LogicalServo:
    def __init__(self, physicalServo: PhysicalServo):
        self._servo = physicalServo

    def setAngle(self, angle: int):
        if angle < 0 or angle > 180:
            raise Exception("Angle out of bounds, expected 0 < angle < 180, was {:d}".format(angle))

        self._servo.setPulse(self._angle2DutyCycle(angle))

    def _angle2DutyCycle(self, angle):
        dutyCycleWidth = self._servo._maxPulse - self._servo._minPulse
        anglePercentage = angle / 180

        return dutyCycleWidth * anglePercentage + self._servo._minDutyCycle
