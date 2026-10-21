#!/usr/bin/env python3

""" jpu's autodrive 21/09/25
This demonstrates usage of motors, sound, sensors, buttons, and leds.
In this demo a basic robot with touch and ultrasonic sensors attachement drives
autonomously. The robot drives forward and slows down when it senses obstacle
ahead (with the infrared sensor). When the obstacle is close it changes
direction randomly. When the obstacle is not detected by the ultrasonic sensor
but bumped by the robot (determined by the touch sensor), it backs up,
then turns in a random direction and continues.
The program may be stopped by pressing any button on the brick. """

from time   import sleep
from random import choice, randint
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, LargeMotor, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor, TouchSensor
from ev3dev2.button import Button
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

# Connect two large motors on output ports B and C:
M = MoveTank(OUTPUT_B, OUTPUT_C)
# Connect ultrasonic and touch sensors.
us = UltrasonicSensor()
ts1 = TouchSensor(INPUT_1)
# We will need to check EV3 buttons state.
btn = Button()

def straight_ahead(speed):
    M.on(left_speed=speed, right_speed=speed)

def backup():
    M.off(brake = True)
    # Turn backup lights on
    for light in ('LEFT', 'RIGHT'):   Leds().set_color(light, 'RED')
    # Sound backup alarm
    Sound().tone([(1000, 100, 100)] * 3)
    # Backup robot
    M.on_for_seconds(left_speed=-50, right_speed=-50, seconds=0.3, brake=True, block=True)
    # Turn backup lights off:
    for light in ('LEFT', 'RIGHT'):   Leds().set_color(light, 'GREEN')

def turn():
    """
    Turn the robot in random direction.
    """
    # We want to turn the robot wheels in opposite directions from 1/4 to 3/4
    # of a second.
    seconds=randint(250, 750)/1000
    #Use `random.choice()` to decide which wheel will turn which way.
    p = choice([(-1), (1)]); left_speed=50*p; right_speed=-50*p;
    M.on_for_seconds(left_speed, right_speed, seconds, brake=True, block=True)


print('Robot Starting')
# Run the robot until a button is pressed.
while not btn.any():
    # if we bump an obstacle: Back away and turn to go in other direction
    if ts1.is_pressed :
        # Backup robot
        backup()
        # Turn robot in random direction
        turn()
        sound= Sound()
        sound.set_volume(100)
        sound.speak("bouge de la !!")

    # Ultrasonic sensor will measure distance to the closest object in front of it
    distance = us.distance_centimeters
    if distance > 40:
        # Path is clear, run at full speed
        straight_ahead(100)
    elif distance > 20:
        # Obstacle ahead, slow down.
        turn()



# Stop the motors before exiting
M.off()
