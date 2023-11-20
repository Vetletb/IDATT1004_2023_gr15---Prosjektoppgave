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



class Farge:
    beholderTid = 1050

    def __init__ (self, farge, beholder, rgbLav, rgbHøy):
        self.farge = farge
        self.beholder = beholder * self.beholderTid - self.beholderTid
        self.rgbLav = rgbLav
        self.rgbHøy = rgbHøy


class FargeRegister:
    def __init__ (self):
        self.fargeDictionary = {}

    def LeggTilFarge(self, farge):
        self.fargeDictionary[farge.farge] = farge

    def HentFarge(self, nøkkel):
        return self.fargeDictionary[nøkkel]


class FargeSorterer:
    avfallBeholder = 2100
    gjeldendeBeholder = 0
    beholderFart = 100
    sorteringTid = 1500
    fargeMargin = 1.25
    samleBåndFart = 50

    def __init__(self, FargeRegister, ev3, samleBånd, beholder, fargeSensor, knapp):
        self.fargeRegister = FargeRegister
        self.ev3 = ev3
        self.samleBånd = samleBånd
        self.beholder = beholder
        self.fargeSensor = fargeSensor
        self.knapp = knapp
        
    def Start(self):
        while not knapp.pressed():
            continue

        wait(2000)
        samleBånd.run(self.samleBåndFart)
        ev3.speaker.set_volume(100)

        while not knapp.pressed():
            while not knapp.pressed():
                rgb = self.StørstFargeVerdi()
                if all(farge > 0 for farge in rgb):
                    print(rgb)
                    for farge in self.fargeRegister.fargeDictionary.values():
                        if self.ErFarge(farge, rgb):
                            print(self.gjeldendeBeholder)
                            break
                else:
                    if self.gjeldendeBeholder - self.avfallBeholder > 0:
                        beholder.run_time(self.beholderFart, abs(self.gjeldendeBeholder - self.avfallBeholder))
                    else:
                        beholder.run_time(-self.beholderFart, abs(self.gjeldendeBeholder - self.avfallBeholder))
                    self.gjeldendeBeholder = self.avfallBeholder

            wait(250)

            self.NullstillBeholder()

            wait(2000)

    def StørstFargeVerdi(self):
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
        
        return [Hrød, Hgrønn, Hblå]

    def ErFarge(self, farge, rgb):
        resultat = False
        rgbLav = [x * (2 - self.fargeMargin) for x in farge.rgbLav]
        rgbHøy = [x * self.fargeMargin for x in farge.rgbHøy]
        if rgb[0] >= rgbLav[0] and rgb[0] <= rgbHøy[0] and rgb[1] >= rgbLav[1] and rgb[1] <= rgbHøy[1] and rgb[2] >= rgbLav[2] and rgb[2] <= rgbHøy[2]:
            resultat = True
            if self.gjeldendeBeholder - farge.beholder > 0:
                beholder.run_time(self.beholderFart, abs(self.gjeldendeBeholder - farge.beholder))
            else:
                beholder.run_time(-self.beholderFart, abs(self.gjeldendeBeholder - farge.beholder))
            ev3.speaker.say(farge.farge)
            wait(self.sorteringTid - abs(self.gjeldendeBeholder - farge.beholder))
            self.gjeldendeBeholder = farge.beholder
            print(farge.farge)
        return resultat

    def NullstillBeholder(self):
        beholder.run_time(self.beholderFart, 4200)
        self.gjeldendeBeholder = 0


class KalibrerFarge:
    def KalibrerFarge():
        while True:
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
            if Hrød > 0 or Hblå > 0 or Hgrønn > 0:
                print(Hrød, Hgrønn, Hblå)

                

rød = Farge("red", 1, [21, 2, 0], [26, 3, 5])
grønn = Farge("green", 2, [7, 20, 4], [10, 27, 11])
gul = Farge("yellow", 4, [42, 34, 15], [51, 38, 20])
oransje = Farge("oransje", 5, [44, 7, 3], [51, 9, 9])

fargeRegister = FargeRegister()

fargeRegister.LeggTilFarge(rød)
fargeRegister.LeggTilFarge(grønn)
fargeRegister.LeggTilFarge(gul)
fargeRegister.LeggTilFarge(oransje)

fargeSorterer = FargeSorterer(fargeRegister, ev3, samleBånd, beholder, fargeSensor, knapp)

fargeSorterer.Start()