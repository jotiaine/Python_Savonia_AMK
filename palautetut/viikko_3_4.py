# -*- coding: utf-8 -*-

"""
KT 4

Kysy käyttäjältä lukujjen määrä ja arvo annettu  kplmäärä  liukulukuja väliltä 1 – 100.
Arvo luku seuraavasti:
    random_decimal = random.randint(100, 10000) / 100
Tulosta arvottu luku käyttäjälle (samalle riville kuin edellinen välilyönnillä erotettuna) ja kirjoita se arvot.txt tiedostoon allekkain.
Jos syötetty luku on < 1, ei ohjelma päättyy ja tulostuu "Virhe!".

Jos tiedosto on jo olemassa, vanhat tiedot menetetään
Älä käytä listaa tms tässä vaiheessa vaan vie luku tiedostoon heti, kun se on arvottu.
Sen jälkeen lue arvot tiedostosta listaan ja lajittele se. Tämän jälkeen tulosta listan  arvot sekä vie
lukujen kplmäärä, summa, keskiarvo, minimiarvo ja maksimiarvo tulokset.txt -tiedostoon
oheisen mallin mukaisesti kahdella desimaalilla (pl kpl):
Kpl: 2
Sum:5.00
Ka: 2.50
Min: 1.00
Max:4.00

Ohessa ajoesimerkki:

Montako lukua arvotaan? 3
Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:
75.41 12.84 17.27
Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:
12.84 17.27 75.41
Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:
Lkm: 3
Sum: 105.52
Ka: 35.17
Min: 12.84
Max: 75.41

Ole taas huolellinen tulostusten kanssa!

"""
import os
import random


def ohjelma():
    tiedosto_arvot = "arvot.txt"
    tiedosto_tulokset = "tulokset.txt"
    arvotLista = []

    wtiedosto_arvot = open(tiedosto_arvot, "w")
    wtiedosto_tulokset = open(tiedosto_tulokset, "w")

    montako = int(input("Montako lukua arvotaan? "))

    if montako < 1:
        print("Virhe!")
        return
    else:
        print("Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:")
        a = 0
        while a < montako:
            arvottava = random.randint(100, 10000) / 100
            print(str(arvottava) + " ", end="")
            wtiedosto_arvot.write(str(arvottava) + "\n")
            a += 1
        wtiedosto_arvot.close()

        arvot = open("arvot.txt", "r")

        for i in arvot:
            arvotLista.append(i.strip())

        arvotLista.sort()
        arvot.close()

        print("\n" + "Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:")
        print(*arvotLista)
        print("Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:")

        float_arvotLista = arvotLista.copy()
        float_new_arvotLista = []
        for i in float_arvotLista:
            float_new_arvotLista.append(float(i))

        summa = float(sum(float_new_arvotLista))
        newSumma = "{:.2f}".format(summa)
        keskiarvo = float(summa / len(arvotLista))
        new_ka = "{:.2f}".format(keskiarvo)
        minimiarvo = float(min(arvotLista))
        min_float = "{:.2f}".format(minimiarvo)
        maximiarvo = float(max(arvotLista))
        max_float = "{:.2f}".format(maximiarvo)

        wtiedosto_tulokset.write("Lkm: " + str(montako) + "\n")
        wtiedosto_tulokset.write("Sum: " + str(newSumma) + "\n")
        wtiedosto_tulokset.write("Ka: " + str(new_ka) + "\n")
        wtiedosto_tulokset.write("Min: " + str(min_float) + "\n")
        wtiedosto_tulokset.write("Max: " + str(max_float) + "\n")

        wtiedosto_tulokset.close()

        print("Lkm: " + str(montako))
        print("Sum: {0:.2f}".format(summa))
        print("Ka: {0:.2f}".format(keskiarvo))
        print("Min: {0:.2f}".format(minimiarvo))
        print("Max: {0:.2f}".format(maximiarvo))


ohjelma()
