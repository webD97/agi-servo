#!/usr/bin/env python3
import time
import math
#from extras import extramath

from physical.PhysicalServo import PhysicalServo
from physical.LogicalServo import LogicalServo
from physical.RoboArm import RoboArm

from Adafruit_PCA9685 import PCA9685

pwm = PCA9685(0x40)
#pwm.set_pwm(5, 0, 600)

armRotation1 = LogicalServo(PhysicalServo(pwm, 5, 400, 2050))
armRotation2 = LogicalServo(PhysicalServo(pwm, 4, 400, 2050))
armRotation3 = LogicalServo(PhysicalServo(pwm, 3, 400, 2050))
armRotation4 = LogicalServo(PhysicalServo(pwm, 2, 400, 2050))
clawRotation = LogicalServo(PhysicalServo(pwm, 1, 350, 1800))
claw = LogicalServo(PhysicalServo(pwm, 0, 350, 1800))

arm = RoboArm(armRotation1, armRotation2, armRotation3, armRotation4, clawRotation, claw)

def reset():
    armRotation4.setAngle(90)
    time.sleep(.5)
    armRotation1.setAngle(90)
    armRotation2.setAngle(90)
    time.sleep(1)
    armRotation3.setAngle(90)
    arm.claw.open()
    arm.claw.setRotation(90)
    time.sleep(2)

def pickupL():
    armRotation1.setAngle(180)
    time.sleep(1)
    armRotation4.setAngle(42) 
    armRotation2.setAngle(9) 
    clawRotation.setAngle(180)
    time.sleep(1)
    armRotation3.setAngle(100)
    time.sleep(1)
    arm.claw.close()
    time.sleep(1)

def pickupR():
    armRotation1.setAngle(0)
    time.sleep(1)
    armRotation2.setAngle(0)
    clawRotation.setAngle(180)
    time.sleep(1)
    armRotation3.setAngle(100)
    armRotation4.setAngle(45)
    time.sleep(1)
    arm.claw.close()
    time.sleep(1)

def slot1():
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
    
    armRotation2.setAngle(147)
    time.sleep(1)
    armRotation4.setAngle(0)
    time.sleep(1)
    armRotation3.setAngle(180)
    time.sleep(2)

def slot2():
      
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
    
    armRotation2.setAngle(115)
    time.sleep(1)
    armRotation4.setAngle(10)
    time.sleep(1)
    armRotation3.setAngle(140)
    time.sleep(5)

def slot3():
     
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
    
    armRotation2.setAngle(95)
    time.sleep(1)
    armRotation4.setAngle(10)
    time.sleep(1)
    armRotation3.setAngle(140)
    time.sleep(.5)

def slot4():
      #Hoch nach pickup:
    
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
    
    armRotation2.setAngle(80)
    time.sleep(1)
    armRotation4.setAngle(10)
    time.sleep(1)
    armRotation3.setAngle(120)
    time.sleep(.5)

def slot5():
  #Hoch nach pickup:
    
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
    
    armRotation2.setAngle(70)
    time.sleep(1)
    armRotation4.setAngle(27)
    time.sleep(1)
    armRotation3.setAngle(120)
    time.sleep(.5)
def slot6():
  #Hoch nach pickup:
    
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
  #Höhe:
    armRotation2.setAngle(70)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation2.setAngle(60)
    time.sleep(1)
    armRotation3.setAngle(110)
    time.sleep(.5)

def slot7():
  
  #Hoch nach pickup:
    
    armRotation2.setAngle(90)
    time.sleep(.05)
    armRotation4.setAngle(20)
    time.sleep(1)
    armRotation4.setAngle(40)
    time.sleep(1)
    armRotation1.setAngle(88)
    #armRotation2.setAngle(60)
    #armRotation3.setAngle(130)
    time.sleep(1)
  #Höhe:
    
    
    armRotation2.setAngle(63)
    time.sleep(1)
    armRotation4.setAngle(60)
    time.sleep(1)
    armRotation2.setAngle(45)
    time.sleep(1)
    armRotation3.setAngle(110)
    time.sleep(.5)
    
    
    

""" Roboter Arm Entrypoint """
def main():
    
    
    pickupL()
    slot6()
    arm.claw.open()
    time.sleep(0.5)
    reset()
    pickupL()
    slot5()
    arm.claw.open()
    time.sleep(0.5)
    reset()
    pickupL()
    slot4()
    arm.claw.open()
    time.sleep(0.5)
    reset()
    pickupL()
    slot3()
    arm.claw.open()
    time.sleep(0.5)
    reset()
    pickupL()
    slot2()
    arm.claw.open()
    time.sleep(0.5)
    reset()
    pickupL()
    slot1()
    arm.claw.open()
    time.sleep(0.5)
    reset()
    
    
    
#    reset()
#    
#    pickupL()
#    slot6()
#    arm.claw.open()
#    time.sleep(1)
    
    
    

    # coords = extramath.cat2sph(10.0, 2.0, 0.0)
    # print("r\t\t= {:f}LE\ninclination\t= {:f}°\nazimuth\t\t= {:f}°".format(coords.radius, math.degrees(coords.inclination), math.degrees(coords.azimuth)))

if __name__ == '__main__':
    main()
