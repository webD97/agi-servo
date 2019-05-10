from .Claw import Claw

from .LogicalServo import LogicalServo

class RoboArm:
    def __init__(self, horizontalMotor: LogicalServo, verticalMotor: LogicalServo, clawRotationMotor: LogicalServo, clawOpenCloseMotor: LogicalServo):
        self._horizontalMotor = horizontalMotor
        self._verticalMotor = verticalMotor
        self._claw: Claw = Claw(clawRotationMotor, clawOpenCloseMotor)

    def moveTo(self, x, y, z):
        pass

    def openClaw(self):
        self._claw.open()

    def closeClaw(self):
        self._claw.close()

    def rotateClaw(self, angle):
        self._claw.setRotation(angle)
