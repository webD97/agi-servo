from .Claw import Claw

from .LogicalServo import LogicalServo

class RoboArm:
    def __init__(self, motor1: LogicalServo, motor2: LogicalServo, motor3: LogicalServo, motor4: LogicalServo, clawRotationMotor: LogicalServo, clawOpenCloseMotor: LogicalServo):
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4
        self.claw: Claw = Claw(clawRotationMotor, clawOpenCloseMotor)

    def moveTo(self, x, y, z):
        raise Exception("Not implemented")
