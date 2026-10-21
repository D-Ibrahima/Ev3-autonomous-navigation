#!/usr/bin/env python3

from time import sleep
from random import choice
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.sensor import INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button

# Initialisation des moteurs et capteurs
M = MoveTank(OUTPUT_B, OUTPUT_C)
cs = ColorSensor(INPUT_3)  # Capteur de couleur sur le port 3
us = UltrasonicSensor(INPUT_4)  # Capteur ultrasonique sur le port 4
btn = Button()

# Seuils de détection des couleurs
BLACK_THRESHOLD = 10   # Intensité lumineuse faible = noir
WHITE_THRESHOLD = 50   # Intensité lumineuse élevée = blanc
RED_COLOR = 5          # Code couleur pour le rouge

def straight_ahead(speed):
    M.on(left_speed=speed, right_speed=speed)

def turn_right():
    M.on(left_speed=50, right_speed=10)

def turn_left():
    M.on(left_speed=10, right_speed=50)

def backup():
    M.off()
    M.on_for_seconds(left_speed=-50, right_speed=-50, seconds=0.5, brake=True, block=True)

def turn():
    """Tourne dans une direction aléatoire après avoir reculé"""
    direction = choice([1, -1])  # Choisir aléatoirement gauche (-1) ou droite (1)
    M.on_for_seconds(left_speed=50 * direction, right_speed=-50 * direction, seconds=0.5, brake=True, block=True)

print("Démarrage du robot...")

while not btn.any():  # Le robot fonctionne jusqu'à ce qu'un bouton soit pressé
    # Vérification des obstacles
    distance = us.distance_centimeters
    if distance < 20:  # Si un obstacle est trop proche
        backup()  # Reculer
        turn()  # Tourner et reprendre la route

    else:
        # Détection de la lumière réfléchie
        light_value = cs.reflected_light_intensity

        if cs.color == RED_COLOR:  # Si du rouge est détecté
            print("ROUGE DÉTECTÉ !")
            M.off()  # Arrêter le robot (ou autre action)

        elif light_value < BLACK_THRESHOLD:  # Ligne noire détectée
            straight_ahead(30)

        elif light_value > WHITE_THRESHOLD:  # Si le robot est complètement sur du blanc
            turn_right()  # Tourne à droite pour retrouver la ligne noire

        else:  # Si le robot est entre les deux (zone grise), ajuste légèrement
            turn_left()

M.off()  # Arrêt du robot quand un bouton est pressé
