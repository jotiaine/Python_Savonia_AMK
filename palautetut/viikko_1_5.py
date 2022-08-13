# -*- coding: utf-8 -*-

"""

KT5

Esittele muuttuja pii, jolle annat alkuarvoksi piin likiarvon 6 desimaalin tarkkuudella.
Lue käyttäjältä ympyrän halkaisija ja tulosta ympyrän piiri ja pinta-ala kahden desimaalin tarkkuudella

Malli ohessa:

Anna ympyrän halkaisija: 12
Piiri on 37.70
Pinta-ala on 113.10

"""

pii = 3.141593
ympyran_halkaisija = float(input("Anna ympyrän halkaisija: "))
sade = ympyran_halkaisija / 2
piiri = round(2 * pii * sade, 2)
pinta_ala = round(pii * (sade ** 2), 2)

print("Piiri on {0:2.2f}\nPinta-ala on {1:2.2f}".format(piiri, pinta_ala))
