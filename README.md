
# Karaktersatt oppgave 1 | DTE-2602

Startkode for å lage en simulering av en robot som utforsker et ukjent terreng. For enkelhets skyld er terrenget delt opp som et rutenett med 36 tilstander. Roboten skal starte i A4 og skal prøve å finne en trygg vei frem til F1.

![image](https://github.com/user-attachments/assets/d30a8ce9-26ed-45d2-a963-ef51c33d1c7a)

Rundt om i terrenget er det ulike hindringer som roboten må ta hensyn til.

![image](https://github.com/user-attachments/assets/1da1c734-8b00-4219-af6e-8ac2ab13dec3)

Roboten klarer å kjøre i bratt terreng, men det krever mye energi og er forbundet med høyere risiko. Roboten er vanntett, men å kjøre gjennom vann krever enda mer energi, og tar svært lang tid sammenliknet med å kjøre på land eller i bratt terreng.
Basert på disse opplysningene kan vi forenkle kartet til følgende figur:
![image](https://github.com/user-attachments/assets/be391153-f986-43b5-8a56-152ca3fdb039)

* Røde ruter er fjell og bratt terreng, og mørkeblå ruter er vann. Hvite ruter er forbundet med lav eller ingen risiko.
* Roboten styres med et API som tillater følgende bevegelser: "opp", "ned", "høyre" og "venstre". Hvis roboten står i rute "A4" og gjør bevegelsen "ned" havner den altså i rute "B4" Roboten kan ikke bevege seg diagonalt.
