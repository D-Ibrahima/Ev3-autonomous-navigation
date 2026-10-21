#!/usr/bin/env python3

from time import sleep
from random import choice
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank
from ev3dev2.motor import LargeMotor
from ev3dev2.sensor import INPUT_3, INPUT_2, INPUT_4
from ev3dev2.sensor.lego import LightSensor
from ev3dev2.button import Button

# Initialisation des moteurs et capteurs
#M = MoveTank(OUTPUT_B, OUTPUT_C)
Motor1=LargeMotor(OUTPUT_C)
Motor2=LargeMotor(OUTPUT_B)
ls1 = LightSensor(INPUT_3)  # droite
ls2 = LightSensor(INPUT_2)  # gauche
btn = Button()
M = MoveTank(OUTPUT_B, OUTPUT_C)

# Seuils de détection de la lumière
light = 50

def stop():
    M.off()


print("Demarrage du robot...")

while not btn.any():  # Le robot fonctionne jusqu'à ce qu'un bouton soit pressé
    light_value1 = ls1.ambient_light_intensity
    light_value2 = ls2.ambient_light_intensity
    speed1=light_value1
    speed2=light_value2
    
    print("Lumiere gauche: ",light_value1," Lumiere droite: ",light_value2)
    
    if light_value1>light or light_value2>light:
        M.off()
    else:
        Motor1.on(speed2*2)
        Motor2.on(speed1*2)
    

M.off()  # Arrêt du robot quand un bouton est pressé
