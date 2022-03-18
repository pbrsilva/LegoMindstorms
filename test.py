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

# Il robot percorre un percorso quadratico
def quadrato():
    #Quadrato
    for i in range(4):
        robot.straight(150)
        robot.turn(95)
def triangolo():
    #Triangolo
    for i in range(3):
        robot.straight(150)
        robot.turn(60)

######### Inizializzazione oggetti #################

ev3 = EV3Brick() #Inizializza mattoncino
left_wheel = Motor(Port.C) #Inizializza motore sinistro
right_wheel = Motor(Port.B) #Inizializza motore sinistro
robot = DriveBase(right_wheel, left_wheel, 55.5, 104) #Inizializza motore

######### Main #################
quadrato() #movimento a forma di quadrato
triangolo()





