# -*- coding: utf-8 -*-

"""
KT6
Kysy käyttäjältä mitä hän haluaa seuraavista vaihtoehdoista (eli käyttäjä syöttää joko numeron 0, 1, 2 tai 3) :

   0 = Lopetus
   1 = Anna säde
   2 = Laske ympyrän piiri
   3 = Laske ympyrän pinta-ala

   Anna valintasi:

Tulosta kysymys edellä kuvatulla tavalla.

Muu kuin 0,1,2,3 vastaa nollaa eli päättää ohjelman toiminnan.

Vaihtoehto 0 päättää ohjelman

Vaihtoehto 1 kysyy ympyrän säteen.  Säteen oletusarvo on nolla (0.0)

Vaihtoehto 2 tulostaa ympyrän piirin (laskukaava on piiri = 2 * pii * säde)

Vaihtoehto 3 tulostaa ympyrän alan (laskukaava on  ala = pii * sade * sade) pinta-ala ja tulosta se.

Jos vaihtoehto on ollut 1,2,3, niin toimenpiteiden (syöttö/tulostus) jälkeen tulostetaan edellä kuvattu  vaihtoehtokysymys uudelleen

Hae piin arvo math moduulista (koodin alkuun import math ja sen jälkeen pii saadaan  math.pi muuttujasta)

Tulosta kaikki desimaaliluvut kahden desimalin tarkkuudella.

Esimerkkiajo ohessa

0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 1
Anna säde: 12


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 2
Piiri on 75.40


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 3
Ala on 452.39


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 0

"""

import math

sade = 0.0

while True:
    vaihtoehto = int(input("""
0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: """))

    if vaihtoehto == 0:
        break
    elif vaihtoehto == 1:
        sade = float(input("Anna säde: "))
    elif vaihtoehto == 2:
        piiri = 2 * math.pi * sade
        print("Piiri on {0:.2f}".format(piiri))
    elif vaihtoehto == 3:
        ala = math.pi * sade**2
        print("Ala on {0:.2f}".format(ala))
    else:
        break
