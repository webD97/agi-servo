from .LogicalServo import LogicalServo

class Claw:
    def __init__(self, rotationServo: LogicalServo, openCloseServo: LogicalServo):
        self._rotationServo = rotationServo
        self._openCloseServo = openCloseServo

    def open(self):
        self._openCloseServo.setAngle(0)

    def close(self):
        self._openCloseServo.setAngle(180)

    def setRotation(self, angle: int):
        self._rotationServo.setAngle(angle)
