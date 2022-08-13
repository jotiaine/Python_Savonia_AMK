# -*- coding: utf-8 -*-

"""

Lue käyttäjältä arvot kahteen lukumuuttujaan. Nimeä muuttujat nimillä eka ja toka sekä alusta ne arvolla nolla.
Tulosta näiden muuttujien summa, erotus ja tulo alla olevalla tavalla (HUOM! Laskutoimituksen tulostus alkaa kaikissa samasta kohdasta!)

Anna eka luku: 10

Anna toka luku: 5

Summa :        10 + 5 = 15

Erotus :       10 - 5 = 5

Tulo :         10 * 5 = 50
"""
eka = 0
toka = 0
eka = int(input("Anna eka luku: "))
toka = int(input("Anna toka luku: "))
summa = eka + toka
erotus = eka - toka
tulo = eka * toka

print("Summa : {0:8} + {1} = {2}".format(eka, toka, summa))
print("Erotus : {0:7} - {1} = {2}".format(eka, toka, erotus))
print("Tulo : {0:9} * {1} = {2}".format(eka, toka, tulo))
