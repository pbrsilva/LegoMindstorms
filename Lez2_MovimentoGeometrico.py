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
        robot.straight(120)
        robot.turn(120)

#Costruisce un poligono regolare dato l'angolo e la lunghezza del lato
def poligonoRegolare(lati, angolo, lunghezza):
    for i in range(lati):
        robot.straight(lunghezza)
        robot.turn(angolo)

######### Inizializzazione oggetti #################

# The DriveBase is composed of two motors, with a wheel on each motor.
# The wheel_diameter and axle_track values are used to make the motors
# move at the correct speed when you give a motor command.
# The axle track is the distance between the points where the wheels
# touch the ground.
ev3 = EV3Brick() #Inizializza mattoncino
left_wheel = Motor(Port.C) #Inizializza motore sinistro
right_wheel = Motor(Port.B) #Inizializza motore sinistro
robot = DriveBase(right_wheel, left_wheel, 55.5, 104) #Inizializza motore
straight_speed = 400 #mm/S
turn_rate = 360 #deg/s

######### Main #################
robot.settings(straight_speed,turn_rate)
quadrato() #movimento a forma di quadrato
triangolo()
poligonoRegolare(6, 60, 80) #esagono





