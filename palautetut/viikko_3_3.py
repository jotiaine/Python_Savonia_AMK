# -*- coding: utf-8 -*-

"""
KT3

Kysy käyttäjältä ensin kieli (Suomi = 0/ Englanti =1). Oletuskieli on suomi, eli muu kuin 0/1 tarkoittaa suomenkielistä tulostusta.
Määrittele koodissa viikonpäivien(ma, ti ke..) tekstit yhteen listaan, jossa on alkio/päivä eli siis molempien kielien viikonpäivänimet (esim Maanatai/Monday].
Kyse on siis rakenteesta lista listassa.

Ota käyttöön muuttuja (dictonary-tyyppinen), johon voit tallentaa maanantain ja perjantain välisenä aikana neljä mittaustulosta
jokaiselta päivältä (mittaustulos on sademäärä milleinä). Lue käyttäjältä nämä mittaustulokset ja
laske vasta lopuksi ja tulosta jokaisen päivän mittaustulosten keskiarvo yhdellä desimaalilla seuraavan esimerkin mukaisesti :

Maanantai:      12.0 mm
Tiistai:        0.0 mm
Keskiviikko:    1.9 mm
Torstai:        22.8 mm
Perjantai:      0.9 mm

Esimerkkiajo ohessa:
Millä kielellä /Please choose language (0 = suomi, 1 = english): 1
Monday 1. : 3
Monday 2. : 2
Monday 3. : 4
... Säästetty tilaa...
Friday 2. : 6
Friday 3. : 5
Friday 4. : 3

Monday 3.5 mm
Tuesday 3.2 mm
Wednesday 4.0 mm
Thursday 4.2 mm
Friday 4.8 mm

Syötteiden järkevyydestä ei tarvitse välittää!

Ole taas huolellinen tulostusten kanssa!

"""

kieli = str(input(
    "Millä kielellä /Please choose language (0 = suomi, 1 = english): "))

if kieli == "1":
    kieliInt = 1
else:
    kieliInt = 0

viikonpaivat = [0, 1]
viikonpaivat[0] = ["Maanantai", "Tiistai",
                   "Keskiviikko", "Torstai", "Perjantai"]
viikonpaivat[1] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

mittaustulokset = {}

for paiva in range(0, 5):
    for mittaustulos in range(0, 4):
        kysy_mittaustulokset = str(
            viikonpaivat[kieliInt][paiva] + " " + str(mittaustulos + 1) + ". : ")
        validointi = (input(kysy_mittaustulokset))
        tulos = float(validointi)
        mittaustulokset.update(
            {viikonpaivat[0][paiva] + str(mittaustulos + 1): tulos})

print()

for paiva in range(0, 5):
    summa = 0.0
    for mittaustulos in range(0, 4):
        key = viikonpaivat[0][paiva] + str(mittaustulos + 1)
        summa += mittaustulokset.get(key)
    keskiarvo = summa / 4
    print(viikonpaivat[kieliInt][paiva], "%.1f" % keskiarvo, "mm")

###
# Toinen tapa
###

# lista = [["Maanantai", "Monday"], ["Tiistai", "Tuesday"], [
#     "Keskiviikko", "Wednesday"], ["Torstai", "Thursday"], ["Perjantai", "Friday"]]
# thisDict = {}

# kieli = int(
#     input("Millä kielellä /Please choose language (0 = suomi, 1 = english): "))

# if kieli != 1:
#     kieli = 0

# for x in lista:
#     summa = 0.0
#     for i in range(1, 5):
#         sadeMaara = float(input(str(x[kieli]) + " " + str(i) + ". : "))
#         summa += sadeMaara
#     keskiarvo = summa / 40
#     thisDict[x[kieli]] = keskiarvo

# for key, value in thisDict.items():
#     print("{0} {1:.1f} mm".format(key, value))
