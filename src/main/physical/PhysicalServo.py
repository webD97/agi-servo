from Adafruit_PCA9685 import PCA9685

class PhysicalServo:
    """ An abstraction for PWM servo motors"""

    def __init__(self, pwm: PCA9685, channel: int, minPulse: int, maxPulse: int, defaultPulse: int = 0):
        """ ctor
                Parameters:
                channel (int): PWM channel
        """
        self._channel = channel
        self._pwm = pwm
        self._minPulse = minPulse
        self._maxPulse = maxPulse
        self._currentPulse = defaultPulse

    def setPulse(self, pulse: int):
        if pulse < self._minPulse or pulse > self._maxPulse:
            raise Exception("Pulse out of bounds: {} < {} < {}".format(self._minPulse, pulse, self._maxPulse))

        self._currentPulse = pulse
        self._pwm.set_pwm(self._channel, 0, int(pulse))

    def changePulse(self, pulse: int):
        newPulse = self._currentPulse + pulse
        if newPulse < self._minPulse or newPulse > self._maxPulse:
            raise Exception("Pulse out of bounds: {} < ({} + {}) < {}".format(self._minPulse, self._currentPulse, pulse, self._maxPulse))

        self._currentPulse = pulse
        self._pwm.set_pwm(self._channel, self._currentPulse, pulse)
