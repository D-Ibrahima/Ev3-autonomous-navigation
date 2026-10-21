#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import GyroSensor
from time import sleep

# Initialisation des moteurs et du bouton
left_motor = LargeMotor(OUTPUT_A)
right_motor = LargeMotor(OUTPUT_D)

def polyg(v, n, dist):
    """ Fonction permettant au robot de dessiner un polygone """
    angle = 360 // n  # Angle de rotation a chaque coin
    s = angle * 14.5 / 2.75  # Calcul pour la rotation precise
    if n==3:
            s=60
    for _ in range(n):
        # Avancer en ligne droite
        left_motor.on_for_degrees(SpeedPercent(v), dist * 360, block=False)
        right_motor.on_for_degrees(SpeedPercent(v), dist * 360, block=True)
        
        # Tourner de l'angle necessaire
        left_motor.on_for_degrees(SpeedPercent(v), s // 2, block=False)
        right_motor.on_for_degrees(SpeedPercent(-v), s // 2, block=True)

def robot(v, n, dist):
    """ Fonction principale qui controle le robot """
    print("Demarrage du robot...")
    
    # Execution une seule fois de la figure
    polyg(v, n, dist)
    
    # Arret des moteurs apres avoir termine la figure
    left_motor.off()
    right_motor.off()
    print("Arret du robot.")
    sleep(1)  # Pause avant la fin du programme pour eviter tout bug

if __name__ == "__main__":
    v = int(input("Vitesse (entre -100 et 100) : "))
    if v < -100 or v > 100:
        print("Erreur : la vitesse doit etre entre -100 et 100.")
        exit()

    n = int(input("Nombre de cotes : "))
    dist = float(input("Distance par cote (en inch) : "))
    
    robot(v, n, dist)
