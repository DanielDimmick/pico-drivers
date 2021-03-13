import machine
import utime
class Stepper:

    def __init__(self, A1, A2, B1, B2, delay):
        self.delay = delay
        self.coil_A_1_pin = machine.Pin(A1, machine.Pin.OUT)
        self.coil_A_2_pin = machine.Pin(A2, machine.Pin.OUT)
        self.coil_B_1_pin = machine.Pin(B1, machine.Pin.OUT)
        self.coil_B_2_pin = machine.Pin(B2, machine.Pin.OUT)
        self.StepCount = 4
        self.Seq = list(range(0, self.StepCount))
        
        self.Seq[0] = [1,0,0,0]
        self.Seq[1] = [0,1,0,0]
        self.Seq[2] = [0,0,1,0]
        self.Seq[3] = [0,0,0,1]

    def release(self):
        self.setStep(0,0,0,0)
        
    def setStep(self, w1, w2, w3, w4):
        self.coil_A_1_pin.value(w1)
        self.coil_A_2_pin.value(w2)
        self.coil_B_1_pin.value(w3)
        self.coil_B_2_pin.value(w4)
     
    def forward(self, steps):
        for i in range(steps):
            for j in range(self.StepCount):
                self.setStep(self.Seq[j][0], self.Seq[j][1], self.Seq[j][2], self.Seq[j][3])
                utime.sleep_ms(self.delay)
     
    def backward(self, steps):
        for i in range(steps):
            for j in reversed(range(self.StepCount)):
                self.setStep(self.Seq[j][0], self.Seq[j][1], self.Seq[j][2], self.Seq[j][3])
                utime.sleep_ms(self.delay)