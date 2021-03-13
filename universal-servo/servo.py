from machine import Pin, PWM

class Servo:
    def __init__(self, pin: int or Pin or PWM, minVal=2500, maxVal=7500, maxDegrees=180):
        if isinstance(pin, int):
            pin = Pin(pin, Pin.OUT)
        if isinstance(pin, Pin):
            self.__pwm = PWM(pin)
        if isinstance(pin, PWM):
            self.__pwm = pin
        self.__pwm.freq(50)
        self.minVal = minVal
        self.maxVal = maxVal
        self.maxDegrees = maxDegrees

    def deinit(self):
        self.__pwm.deinit()

    def goto(self, value: int):
        delta = self.maxVal-self.minVal
        target = int(self.minVal + ((value / 1024) * delta))
        self.__pwm.duty_u16(target)

    def gotoDeg(self, value: int):
        diff = int(self.maxVal - self.minVal)
        oneDegree = int(diff/self.maxDegrees)
        self.__pwm.duty_u16(self.minVal+(oneDegree*value))

    def free(self):
        self.__pwm.duty_u16(0)