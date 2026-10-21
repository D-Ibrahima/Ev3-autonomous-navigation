#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button

# Initialisation des moteurs et du capteur de couleur
M = MoveTank(OUTPUT_B, OUTPUT_C)
cs = ColorSensor(INPUT_3)  # Assurez-vous que le capteur est bien connecté au port 3
btn = Button()

# Seuil pour détecter le noir et le blanc (à ajuster selon l'éclairage)
BLACK_THRESHOLD = 10  # Intensité de lumière basse pour noir
WHITE_THRESHOLD = 50  # Intensité de lumière haute pour blanc

def straight_ahead(speed):
    M.on(left_speed=speed, right_speed=speed)

def turn_right():
    M.on(left_speed=50, right_speed=10)

def turn_left():
    M.on(left_speed=10, right_speed=50)

print("Démarrage du suiveur de ligne...")

while not btn.any():  # Arrêt si un bouton est pressé
    light_value = cs.reflected_light_intensity  # Récupération de l'intensité lumineuse

    if light_value < BLACK_THRESHOLD:  # Si on est sur la ligne noire
        straight_ahead(30)
    else:  # Si on est sur du blanc, corriger la trajectoire
        if light_value > WHITE_THRESHOLD:  # Si c'est blanc (peut nécessiter un ajustement)
            turn_right()
        else:
            turn_left()

M.off()  # Arrêt du robot quand le programme est terminé