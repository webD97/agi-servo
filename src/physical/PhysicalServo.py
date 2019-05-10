class PhysicalServo:
    """ An abstraction for PWM servo motors"""

    def __init__(self, minDutyCycle: int, maxDutyCycle: int, frequency: int, channel: int):
        """ ctor

                Parameters:
                minDutyCycle (int): The duty cycle for the outermost left postion
                maxDutyCycle (int): The duty cycle for the outermost right postion
                frequency (int): PWM frequency [Hz]
                channel (int): PWM channel
        """
        self._minDutyCycle: int = minDutyCycle
        self._maxDutyCycle: int = maxDutyCycle
        self._frequency: int = frequency
        self._channel: int = channel

        self._currentDutyCycle: int = minDutyCycle

        # Initialize PWM thing here

    def setDutyCycle(self, dutyCycle: int):
        if dutyCycle < self._minDutyCycle or dutyCycle > self._maxDutyCycle:
            raise Exception(
                "Given DutyCycle out of bounds! Value was {:d}".format(dutyCycle))

        self._currentDutyCycle = dutyCycle

        # Update PWM signal here
