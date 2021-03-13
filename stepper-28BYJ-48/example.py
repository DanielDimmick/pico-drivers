import utime
import machine
from sm28byj48 import *

# Coil A1 pin, Coil A2 pin,  Coil B1 pin, Coil B2 pin, delay ms
# Note this is not using PWM, this stepper cannot respond faster than 3ms so delay is set to 3
motor = Stepper(12,13,14,15,3)

# the number of steps to move forward / backward
motor.forward(512)
motor.backward(512)