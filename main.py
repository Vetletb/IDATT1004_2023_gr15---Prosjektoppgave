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

rødBeholder = 0
blåBeholder = 1050
avfallBeholder = 2100
grønnBeholder = 3150
ukjentBeholder = 4200

gjeldendeBeholder = 0
fart = 100
sorteringTid = 1000

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
                wait(sorteringTid - (gjeldendeBeholder - rødBeholder))
                gjeldendeBeholder = rødBeholder
                print("rød")
            elif blå * 100 / sum >= 50 and blå > 3:
                if gjeldendeBeholder - blåBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - blåBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - blåBeholder))
                ev3.speaker.say("blue")
                wait(sorteringTid - (gjeldendeBeholder - blåBeholder))
                gjeldendeBeholder = blåBeholder
                print("blå")
            elif grønn * 100 / sum >= 50 and grønn > 3:
                if gjeldendeBeholder - grønnBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - grønnBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - grønnBeholder))
                ev3.speaker.say("green")
                wait(sorteringTid - (gjeldendeBeholder - grønnBeholder))
                gjeldendeBeholder = grønnBeholder
                print("grønn")
        else:
            if gjeldendeBeholder - avfallBeholder > 0:
                beholder.run_time(fart, abs(gjeldendeBeholder - avfallBeholder))
            else:
                beholder.run_time(-fart, abs(gjeldendeBeholder - avfallBeholder))
            gjeldendeBeholder = avfallBeholder
            print("avfall")

        wait(250)
    beholder.run_time(fart, 4200)
    gjeldendeBeholder = avfallBeholder
    wait(2000)