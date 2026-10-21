from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import LightSensor
import time

# Initialisation des moteurs et du capteur de couleur
motor_pair = MoveTank(OUTPUT_B, OUTPUT_C)
color_sensor = LightSensor(INPUT_3)

# Définition de la couleur rouge selon le capteur
RED_THRESHOLD = 5  # Ajuste cette valeur selon ton capteur

# Vitesses des moteurs
BASE_SPEED = 30  # Vitesse normale
TURN_SPEED = 10  # Vitesse pour corriger la trajectoire

while True:
    color = color_sensor.color
    
    if color == RED_THRESHOLD:
        # Avancer tout droit
        motor_pair.on(BASE_SPEED, BASE_SPEED)
    else:
        # Ajustement : tourner légèrement
        motor_pair.on(TURN_SPEED, BASE_SPEED)
    
    time.sleep(0.05)  # Petite pause pour éviter une boucle trop rapide
