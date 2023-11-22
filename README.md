# IDATT1004_2023_gr15 - Prosjektoppgave


## Fargesorteringsmaskin
En Farge sorterer

## Beskrivelse
Sorterer ulike objekter som legges på samlebåndet i en av fire ulike beholdere etter farge. Ved uønskede farger vil disse bli sortert i en egen avfallsbeholder, så du kan nyte en feilfri sortering. Sorteren har en rekke avanserte funksjonaliteter. Den vil sortere opptil fire farger etter forhåndskalibrerte verdier (skittles kommer som standard), eventuelt så mange farger du vil fordelt på de fire beholderne. Du har også muligheten til å manuelt tilbakestille sortereren ved feil under sortering. ps. programmet fungerer ekslusivt på fargesorteringsmaksinen til Team 15.


## Video og bilder
![oversiktsbilde](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/blob/main/Media/Bilde1.jpg?raw=true)

Sorterer skittles etter farge og kaster nonstop i avfall.
![Video demo](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/blob/main/Media/10000000_24234439519504156_1795635800846122043_n.mp4?ref_type=heads?raw=true)


## Installasjon
Når du har mottatt din splitter nye fargesorteringsmaskin er det svært enkelt å sette i gang. Først må du plugge inn den medfølgende laderen. Maskinen er oppladet, kan den enkelt skrus på ved å trykke på den runde knappen på ev3-en. Programmet kommer ferdig installert i maskinen og du trenger kun starte programmet. Dette gjøres ved å velge "files" fra menyen og navigere til "idatt1003_2023_gr15/main.py". Tilse at beholderen er plassert helt til venstre. Maskinen er nå klar til bruk!


## Bruker instruksjoner
Under vil du finne informasjon om hvordan du benytter deg av de ulike funskjonaliteten til fargesorteren.


### Slå på/av
Etter at installasjonsprossesen er ferdig, er du klar til å starte maskinen. Dette gjøres enkelt ved å trykke på den røde knappen, vent til beholderen er i startposisjon (når beholderen er sentrert om samlebåndet). Maskinen kan slås av igjen ved å holde inne den samme knappen i 2-3 sekunder.


### Sortere skittles
For å sortere en skittle trenger du kun legge den ned på starten av samlebåndet, vent med å legge på en ny til beholderen har er tilbake i startposisjon.


### Manuelt tilbakestille beholderposjisjon
Hvis du skulle oppdage at beholderens posisjon har blitt usynkronisert med der programmet tror den er lokalisert (beholderen går ikke tilbake til startposisjon), kan på knappen trykkes inn for å tilbakestille beholderen.


## Støtte
Team 15 går dessverre i oppløsning 24. november, det vil ikke være mulighet for å kontakte oss ved eventuelle feil eller spørsmål fra denne datoen.


## Forfattere
Fargesorteringsmaskinen er utviklet av de flotte medlemmene av Team 15; [Vetle Traran Bjørnøy](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/wikis/About-team/Vetle%20Traran%20Bjørnøy), [Hong An Ho](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/wikis/About-team/Hong-An-Ho), [Edvard Granheim Harbo](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/wikis/About-team/Edvard-Granheim-Harbo), [Cathrine Evensen](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/wikis/About-team/Cathrine-Evensen) og [Carine Margrethe Rondeel](https://gitlab.stud.idi.ntnu.no/carinemr/idatt1004_2023_gr15-prosjektoppgave/-/wikis/About-team/Carine-Margrethe-Rondeel).


## Produkt status
Produktet er ferdig konstruert og programmert, og vil ikke bli videre støttet eller utviklet av utviklerene.


## FAQ
Kan jeg sortere andre ting enn skittles?
 - Ja, dette kan fikses ved etterspørsel ved bestilling av produktet, eller av en som har fått opplæring i kalibrering.

Hva skjer om jeg mister en non-stop eller annet objekt som ikke er ment å sorteres?
 - Fortvil ikke, hvis noe havner i sorteren som ikke skal sorteres vil de bli ignorert og havner i avfallsbeholderen.

Hva skjer om jeg legger på en ny skittles før maskinen er klar for å sortere en ny?
 - Konsekvensen avhenger av hvor tidlig den ble lagt på, den vil enten havne i feil fargebeholder hvis beholderen ikke rekker å komme tilbake til start, eller så vil den simpelt havne i avfallsbeholderen. 

Hvorfor sluttet sorteren å sortere riktig?
 - Hvis fargesorteren slutter å fungere kan dette være tegn på at en ny kalibrering er nødvendig. Dette kan være forårsaket av endring i miljø, eller at fargesensoren ikke leser samme verdier som sist den ble kalibrert. Se "støtte" for hjelp