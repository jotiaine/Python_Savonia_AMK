# -*- coding: utf-8 -*-

"""
KT2
Lue käyttäjältä koenumero 4-10 väliltä. Jos käyttäjä syötti arvosanan väärin (ei väliltä 4-10) , niin tulosta "Et antanut arvosanaa annetulta väliltä". Muussa tapauksessa tulosta:

 Hyvä (jos arvosana oli 9 tai 10)

 Kelpo (jos 7 - 8)

 Tyydyttävä (jos 5 - 6)

 Heikko (jos 4)

 Toteuta ohjelma if-elif-else -rakenteella.

 Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin.

 
"""

koenumero = int(input("Anna koe arvosana: "))

if koenumero == 9 or koenumero == 10:
    print("Hyvä")
elif koenumero == 7 or koenumero == 8:
    print("Kelpo")
elif koenumero == 6 or koenumero == 5:
    print("Tyydyttävä")
elif koenumero == 4:
    print("Heikko")
else:
    print("Et antanut arvosanaa annetulta väliltä")
