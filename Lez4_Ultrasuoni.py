#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def stopColor():
    while(color_sens.color() != Color.BLACK):
        robot.drive(100, 0)
    robot.stop()
    left_wheel.brake()
    right_wheel.brake()


ev3 = EV3Brick() #Inizializza mattoncino
left_wheel = Motor(Port.C) #Inizializza motore sinistro
right_wheel = Motor(Port.B) #Inizializza motore sinistro
robot = DriveBase(right_wheel, left_wheel, 55.5, 104) #Inizializza motore
straight_speed = 400 #mm/S
turn_rate = 360 #deg/s
drive_speed = 0 #mm/s
drive_turn_rate = 80 #deg/s
color_sens = ColorSensor(Port.S3)

stopColor()

