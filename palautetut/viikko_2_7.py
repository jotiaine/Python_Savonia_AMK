# -*- coding: utf-8 -*-

"""
KT7

Toimeentulotukea maksetaan turvaamaan perustuslaissa tarkoitettu välttämätön toimeentuloa.
Tee ohjelma, joka laskee yksinäisen henkilön tai perheen saaman toimeentulotuen.
Ohjelma laskee tuen määrän käyttäjän syöttämälle määrälle päiviä ja tulostaa toimeentulotuen kokonaismäärän kahdella desimaalilla.
Ohjelma kysyy tuen laskemisessa tarvittavat tiedot yhdessä asumisesta ja lapsista.
Toimeentulotuen määrä lasketaan alla olevan taulukon mukaisesti kahden desimaalin tarkkuudella.
Toimeentulotuen laskemista voidaan toistaa niin monta kertaa kuin ohjelman käyttäjä haluaa. Alla on suuntaa antava esimerkki ohjelman toiminnasta.

Tuki lasketaan siis yhdelle henkilölle, ei esim avioparille


Tuen saaja

Euroa / päivä

Yksin asuva

16,18

Yksinhuoltaja

17,80

Avio- ja avopuolisot kumpikin

13,76

Jokainen 10-17-vuotias lapsi

11,33

Jokainen alle 10-vuotias lapsi

10,20



Tämä ohjelma laskee toimeentulotuen määrän. Alla esimerkkiajo ohjelmasta.

Koodin rakenteelle ei aseteta vaatimuksia muuten kuin, että syötteet annetaan esimerkin mukaisessa järjestyksessä ja ohjelma laskee (tulostaa) tuen määrän oikein. Esimerkkiajosta käy ilmi. että kysymyksiä luupataan eli ohjelma päättyy vasta kun  käyttäjä ei halua enää laskea toimeentulotukea uusilla tiedoilla.



Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): k

Asutko yksin (1) vai puolison kanssa (2) : 1

Onko sinulla/teillä alaikäisiä lapsia (k/e) : k

Kuinka monta alle 10-vuotiasta lasta : 1

Kuinka monta 10-17-vuotiasta lasta : 2

Kuinka monelle päivälle tuki lasketaan : 10



Saat toimeentulotukea 506.60 euroa

Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): e

"""


def laske_toimeentulotuki():
    while True:
        euroa_paivassa = 0
        laskeeko = input(
            "Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): ")

        if(laskeeko == "k"):
            # YKSIN?
            yksin_asuva = input("Asutko yksin (1) vai puolison kanssa (2) : ")
            if(yksin_asuva == "1"):
                euroa_paivassa += 16.18

                # LAPSIA?
                lapsia = input(
                    "Onko sinulla/teillä alaikäisiä lapsia (k/e) : ")
                if(lapsia == "k"):
                    euroa_paivassa = 17.80
                    alle10v_lapsia = int(
                        input("Kuinka monta alle 10-vuotiasta lasta : "))
                    euroa_paivassa += (alle10v_lapsia * 10.20)
                    lapsiaValilta10_17 = int(
                        input("Kuinka monta 10-17-vuotiasta lasta : "))
                    euroa_paivassa += (lapsiaValilta10_17 * 11.33)

                    # PÄIVÄT?
                    paivat = int(
                        input("Kuinka monelle päivälle tuki lasketaan : "))

                    # Printataan tulos
                    toimeentulotuki = euroa_paivassa * paivat
                    print("Saat toimeentulotukea {0:.2f} euroa".format(
                        toimeentulotuki))
                else:
                    # PÄIVÄT?
                    paivat = int(
                        input("Kuinka monelle päivälle tuki lasketaan : "))

                    # Printataan tulos
                    toimeentulotuki = euroa_paivassa * paivat
                    print("Saat toimeentulotukea {0:.2f} euroa".format(
                        toimeentulotuki))
            else:
                euroa_paivassa += 13.76

                # LAPSIA?
                lapsia = input(
                    "Onko sinulla/teillä alaikäisiä lapsia (k/e) : ")
                if(lapsia == "k"):
                    alle10v_lapsia = int(
                        input("Kuinka monta alle 10-vuotiasta lasta : "))
                    euroa_paivassa += (alle10v_lapsia * 10.20)
                    lapsiaValilta10_17 = int(
                        input("Kuinka monta 10-17-vuotiasta lasta : "))
                    euroa_paivassa += (lapsiaValilta10_17 * 11.33)

                # PÄIVÄT?
                paivat = int(
                    input("Kuinka monelle päivälle tuki lasketaan : "))

                # Printataan tulos
                toimeentulotuki = euroa_paivassa * paivat
                print("Saat toimeentulotukea {0:.2f} euroa".format(
                    toimeentulotuki))
        else:
            break


laske_toimeentulotuki()
