#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from time import sleep

# Initialisation
left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_D)
M = MoveTank(OUTPUT_A, OUTPUT_D)
angle = 90  # Angle de rotation a chaque coin
s = angle * 14.5 / 2.75  # Calcul pour la rotation precise



# Fonction pour tourner à gauche
def tourner_gauche_90():
    left_motor.on_for_degrees(SpeedPercent(10), s // 2, block=False)
    right_motor.on_for_degrees(SpeedPercent(-10), s // 2, block=True)

# Fonction pour tourner à droite
def tourner_droite_90():
    left_motor.on_for_degrees(SpeedPercent(-10), s // 2, block=False)
    right_motor.on_for_degrees(SpeedPercent(10), s // 2, block=True)

# Fonction pour avancer d'une distance donnée (en inch)
def movethank(speed, distance):
    rotations = distance / 2.75
    M.on_for_rotations(SpeedPercent(speed), SpeedPercent(speed), rotations, brake=True, block=True)

# Fonction principale
def lab(speed):
    movethank(speed, 5.7)
    tourner_droite_90()
    movethank(speed, 5.6)
    tourner_gauche_90()
    movethank(speed, 4.5)
    tourner_gauche_90()
    movethank(speed, 4.7)
    tourner_droite_90()
    movethank(speed, 17)
    tourner_droite_90()
    movethank(speed, 5.4)
    tourner_droite_90()
    movethank(speed, 5.4)
    tourner_gauche_90()
    movethank(speed, 5.4)
    tourner_droite_90()
    movethank(speed, 4)
    tourner_droite_90()
    movethank(speed, 4)
    tourner_gauche_90()
    movethank(speed, 4)
    tourner_gauche_90()
    movethank(speed, 4)
    tourner_droite_90()
    movethank(speed, 5.7)

lab(10)

# Arrêt des moteurs
M.off()