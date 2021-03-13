from servo import Servo
from machine import Pin
import utime

# Set to your specific servo requirements
# (pin number, minimum duty, maximum duty, range of motion in degrees)
s1 = Servo(2,1700,8150,180) 

while True:
    # Go to specific degrees
    s1.gotoDeg(0)
    utime.sleep(2)
    s1.gotoDeg(90)
    utime.sleep(2)
    s1.gotoDeg(180)
    utime.sleep(2)
    s1.gotoDeg(90)
    utime.sleep(2)
    
    # Go to range between 0 and 1024
    s1.goto(0)
    utime.sleep(2)
    s1.goto(512)
    utime.sleep(2)
    s1.goto(1024)
    utime.sleep(2)
    s1.goto(512)
    utime.sleep(2)
