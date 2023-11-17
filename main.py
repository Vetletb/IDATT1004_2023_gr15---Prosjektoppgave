#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#Lager motorer og sensorer
ev3 = EV3Brick()
samleBånd = Motor(Port.B)
beholder = Motor(Port.D)
fargeSensor = ColorSensor(Port.S3)
knapp = TouchSensor(Port.S2)

#Verdier for plassering av beholdere målt i ms
rødBeholder = 0
grønnBeholder = 1050
avfallBeholder = 2100
gulBeholder = 3150
oransjeBeholder = 4200

#Standard verdier
gjeldendeBeholder = 0
fart = 100
sorteringTid = 1500
fargeMargin = 1.25

#Kalibrerings verdier

rødRødL = 21 * (2 - fargeMargin)
rødRødH = 26 * fargeMargin
rødGrønnL = 2 * (2 - fargeMargin)
rødGrønnH = 3 * fargeMargin
rødBlåL = 0 * (2 - fargeMargin)
rødBlåH = 5 * fargeMargin

grønnRødL = 7 * (2 - fargeMargin)
grønnRødH = 10 * fargeMargin
grønnGrønnL = 20 * (2 - fargeMargin)
grønnGrønnH = 27 * fargeMargin
grønnBlåL = 4 * (2 - fargeMargin)
grønnBlåH = 11 * fargeMargin

gulRødL = 42 * (2 - fargeMargin)
gulRødH = 51 * fargeMargin
gulGrønnL = 34 * (2 - fargeMargin)
gulGrønnH = 38 * fargeMargin
gulBlåL = 15 * (2 - fargeMargin)
gulBlåH = 20 * fargeMargin

oransjeRødL = 44 * (2 - fargeMargin)
oransjeRødH = 51 * fargeMargin
oransjeGrønnL = 7 * (2 - fargeMargin)
oransjeGrønnH = 9 * fargeMargin
oransjeBlåL = 3 * (2 - fargeMargin)
oransjeBlåH = 9 * fargeMargin

#Starter programmet når knapp presses
while not knapp.pressed():
    continue

wait(2000)
samleBånd.run(50)
ev3.speaker.set_volume(100)

#Sorterer
while not knapp.pressed():
    while not knapp.pressed():
        
        #finner største fargeverdi registert
        (rød, grønn, blå) = fargeSensor.rgb()
        Hrød = 0
        Hgrønn = 0
        Hblå = 0
        sum = blå + grønn + rød
        while rød > 13 or blå > 13 or grønn > 13:
            if rød > 10 or blå > 10 or grønn > 10:
                if rød + blå + grønn >= sum:
                    sum = rød + blå + grønn
                    (Hrød, Hgrønn, Hblå) = (rød, grønn, blå) 
                (rød, grønn, blå) = fargeSensor.rgb()
        if Hrød > 0 or Hgrønn > 0 or Hblå > 0:
            print(Hrød, Hgrønn, Hblå)
            #sjekker om rød
            if Hrød >= rødRødL and Hrød <= rødRødH and Hgrønn >= rødGrønnL and Hgrønn <= rødGrønnH and Hblå <= rødBlåH:
                if gjeldendeBeholder - rødBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - rødBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - rødBeholder))
                ev3.speaker.say("red")
                wait(sorteringTid - abs(gjeldendeBeholder - rødBeholder))
                gjeldendeBeholder = rødBeholder
                print("rød")

            #sjekker om grønn
            elif Hrød >= grønnRødL and Hrød <= grønnRødH and Hgrønn >= grønnGrønnL and Hgrønn <= grønnGrønnH and Hblå >= grønnBlåL and Hblå <= grønnBlåH:
                if gjeldendeBeholder - grønnBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - grønnBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - grønnBeholder))
                ev3.speaker.say("green")
                wait(sorteringTid - abs(gjeldendeBeholder - grønnBeholder))
                gjeldendeBeholder = grønnBeholder
                print("grønn")

            #sjekker om gul
            elif Hrød >= gulRødL and Hrød <= gulRødH and Hgrønn >= gulGrønnL and Hgrønn <= gulGrønnH and Hblå >= gulBlåL and Hblå <= gulBlåH:
                if gjeldendeBeholder - gulBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - gulBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - gulBeholder))
                ev3.speaker.say("yellow")
                wait(sorteringTid - abs(gjeldendeBeholder - gulBeholder))
                gjeldendeBeholder = gulBeholder
                print("gul")

            #sjekker om oransje
            elif Hrød >= oransjeRødL and Hrød <= oransjeRødH and Hgrønn >= oransjeGrønnL and Hgrønn <= oransjeGrønnH and Hblå >= oransjeBlåL  and Hblå <= oransjeBlåH:
                if gjeldendeBeholder - oransjeBeholder > 0:
                    beholder.run_time(fart, abs(gjeldendeBeholder - oransjeBeholder))
                else:
                    beholder.run_time(-fart, abs(gjeldendeBeholder - oransjeBeholder))
                ev3.speaker.say("orange")
                wait(sorteringTid - abs(gjeldendeBeholder - oransjeBeholder))
                gjeldendeBeholder = oransjeBeholder
                print("oransje")

        #Hvis ingen farge, flytt til avfallbeholder
        else:
            if gjeldendeBeholder - avfallBeholder > 0:
                beholder.run_time(fart, abs(gjeldendeBeholder - avfallBeholder))
            else:
                beholder.run_time(-fart, abs(gjeldendeBeholder - avfallBeholder))
            gjeldendeBeholder = avfallBeholder

        wait(250)

    #Hvis knapp trykkes nullstill beholderposisjon
    beholder.run_time(fart, 4200)
    gjeldendeBeholder = 0
    #Hvis knapp fortsatt holdes inne etter 2 sek, avslutt program
    wait(2000)


# while True:
#     (rød, grønn, blå) = fargeSensor.rgb()
#     Hrød = 0
#     Hgrønn = 0
#     Hblå = 0
#     sum = blå + grønn + rød
#     while rød > 13 or blå > 13 or grønn > 13:
#         if rød > 10 or blå > 10 or grønn > 10:
#             if rød + blå + grønn >= sum:
#                 sum = rød + blå + grønn
#                 (Hrød, Hgrønn, Hblå) = (rød, grønn, blå) 
#             (rød, grønn, blå) = fargeSensor.rgb()
#     if Hrød > 0 or Hblå > 0 or Hgrønn > 0:
#         print(Hrød, Hgrønn, Hblå)

