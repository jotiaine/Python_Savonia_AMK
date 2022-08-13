# -*- coding: utf-8 -*-

#
# KT1
#
# Luo aluksi tyhjä lista (muuttujanimi: luvut) ja lue siihen käyttäjältä 5 kokonaislukuarvoa.
# Tulosta lopuksi syötettyjen lukujen summa (kokonaislukuna) ja keskiarvo kolmella desimaalilla
#
# Esimerkkiajo ohessa
#
# Anna luku: 1
# Anna luku: 2
# Anna luku: 3
# Anna luku: 4
# Anna luku: 5
# Summa on: 15
# Keskiarvo on: 3.000
#

luvut = []
luku1 = luvut.append(int(input("Anna luku: ")))
luku2 = luvut.append(int(input("Anna luku: ")))
luku3 = luvut.append(int(input("Anna luku: ")))
luku4 = luvut.append(int(input("Anna luku: ")))
luku5 = luvut.append(int(input("Anna luku: ")))

summa = 0

for x in luvut:
    summa += x

keskiarvo = summa / 5

print("Summa on:", summa)
print("Keskiarvo on: {0:.3f}".format(keskiarvo))
