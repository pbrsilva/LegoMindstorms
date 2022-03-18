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

# Ruota il motore di un dato angolo e velocità
def testMotore1():
    motor.run_angle(360, 720) # compie 2 giri in 2 secondo
    motor.run_angle(720, 720) # compie 2 giri in 1 secondo
    motor.run_angle(-360, 720) # compie 2 giri in senso opposto in 2 secondi
    motor.run_time(360, 3000) # ruota alla velocità di un giro al secondo per 3 secondi
    motor.run(360) # ruota per 10 secondi
    wait(10000)

# Inizializza un sensore Touch e riproduce un beep ad ogni pressione del sensore ad una frequenza crescente
# partendo dalla nota Do centrale (262 Hz)
def testTouch():
    f = 262 #Do
    i = 0
    while(i < 10):
        if touch_sens.pressed():
            ev3.speaker.beep(f)
            f += 16
            i += 1
# "Ventilatore" con 3 velocità e spegnimento grazie al sensore di tocco
def ventilatore():
    speed = 0
    while(speed < 180 * 4):
        if(touch_sens.pressed()):
            wait(500)
            speed += 180
            print(str(speed))
            motor.brake()           
        motor.run(speed)
    ev3.speaker.say(str(speed))               


# Testa le differenze tra i tipi diversi di frenata
def testFrenate():
    #COAST
    motor.stop()
    motor.run_target(500, 180, Stop.COAST)
    wait(3000)
    #BREAK
    motor.brake()
    motor.run_target(500, 0, Stop.BRAKE)
    wait(3000)

# Inizializza un motore e compie un movimento "a tergicristallo"
def tergicristallo():
    angle = 180
    speed = 360 # 1 giro al secondo
    for i in range(10):
        motor.run_angle(speed, angle, Stop.BRAKE)
        angle *= -1

# Azionare moviemento a tergicristallo in base al colore
def testColor():
    while(True):
        if (color_sens.color() == Color.RED):
            tergicristallo()

def motoreDritto():
    motor_right.run_time(speed=180,time=2000)
    motor_left.run_time(speed=180,time=2000)

# riproduci i vari esercizi intervallati da un "beep"
ev3 = EV3Brick() # Inizializza il mattoncino EV3 
motor = Motor(Port.D) # Inizializza il motore sulla porta
motor_right = Motor(Port.C)
motor_left = Motor(Port.B)
touch_sens = TouchSensor(Port.S1) # Inizializza il sensore Touch
color_sens = ColorSensor(Port.S3) # Inizializza il sensore di Colore

# motore che esegue semplici rotazioni
ventilatore()
testMotore1()
motoreDritto()
ev3.speaker.beep()
# differenze di frenata
testFrenate()
ev3.speaker.beep()
# motore che simula il tergicristallo
tergicristallo() 
ev3.speaker.beep()
# sensore touch che suona una nota crescente
testTouch() 
testColor()




