#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
samleBånd = Motor(Port.B)
beholder = Motor(Port.D)
fargeSensor = ColorSensor(Port.S3)
knapp = TouchSensor(Port.S2)

avfallBeholder = 0
rødBeholder = 1050
blåBeholder = 2100
grønnBeholder = 3150
ukjentBeholder = 4200

gjeldendeBeholder = rødBeholder
fart = 100
sorteringTid = 5000

while not knapp.pressed():
    continue

wait(2000)
samleBånd.run(50)
ev3.speaker.set_volume(100)

while not knapp.pressed():
    while not knapp.pressed():
        (rød, grønn, blå) = fargeSensor.rgb()
        print(rød, grønn, blå)
        sum = rød + blå + grønn
        if sum > 3:
            if rød * 100 / sum >= 50 and rød > 3:
                if gjeldendeBeholder - rødBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - rødBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - rødBeholder))
                ev3.speaker.say("red")
                wait(gjeldendeBeholder - rødBeholder)
                gjeldendeBeholder = rødBeholder
            elif blå * 100 / sum >= 50 and blå > 3:
                if gjeldendeBeholder - blåBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - blåBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - blåBeholder))
                ev3.speaker.say("blue")
                wait(gjeldendeBeholder - blåBeholder)
                gjeldendeBeholder = blåBeholder
            elif grønn * 100 / sum >= 50 and grønn > 3:
                if gjeldendeBeholder - grønnBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - grønnBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - grønnBeholder))
                ev3.speaker.say("green")
                wait(gjeldendeBeholder - grønnBeholder)
                gjeldendeBeholder = grønnBeholder
            else: {
                if gjeldendeBeholder - avfallBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - avfallBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - avfallBeholder))
                wait(sortereTid - (gjeldendeBeholder - avfallBeholder))
                gjeldendeBeholder = avfallBeholder
            }
        wait(250)
    beholder.run_time(fart, 4200)
    gjeldendeBeholder = AvfallBeholder
    wait(2000)