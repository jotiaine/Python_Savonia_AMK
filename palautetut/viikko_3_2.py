# -*- coding: utf-8 -*-

#
# KT2
#
# Kysy käyttäjältä, montako lukua arvotaan.Jos käyttäjä syöttää arvon < 1, tulostuu "Virhe!"
# Tee lista ja arvo siihen em määrä lukuja  väliltä 0-20.
# Vain parilliset luvut sallitaan.
# Jos arvottiin pariton luku niin sen tilalle on arvottava uusi luku.
# Tulosta luvuista suurin ja pienein samalle riville
# Ja lopuksi tulosta arvotut luvut yhdelle riville pilkulla erotettuna
# Huomaa, että viimeisen luvun jälkeen ei tule pilkkua
#
# Esimerkkiajo ohessa
#
# Montako lukua arvotaan: 3
# Suurin: 6 ja pienin: 0
# 4,0,6
#
import random


def ohjelma():
    montako = int(input("Montako lukua arvotaan: "))
    if(montako < 1):
        print("Virhe!")
        return
    else:
        lista = []

        def random_numero():
            arvottuLuku = random.randint(0, 20)
            if arvottuLuku % 2 != 0:
                while True:
                    arvottuLuku = random.randint(0, 20)
                    if arvottuLuku % 2 == 0:
                        break
            return arvottuLuku

        def lisaaLuvutListaan():
            for i in range(montako):
                randomNumero = random_numero()
                # Lisätään listaan arvottu parillinen luku
                lista.append(randomNumero)

        lisaaLuvutListaan()

        suurin = max(lista)
        pienin = min(lista)

        print("Suurin: " + str(suurin) + " ja pienin: " + str(pienin))

        # for x in range(len(lista)):
        #     if(x == (len(lista) - 1)):
        #         print(lista[x])
        #     else:
        #         print(lista[x], end=",")

        uusi_lista = [str(a) for a in lista]
        print(",".join(uusi_lista))


ohjelma()
