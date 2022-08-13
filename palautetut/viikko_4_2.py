"""
KT2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5, niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi annetaan LOPPU. 

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana). Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn saaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn 
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita 

"""

# Write functions here!


def LuoNimetJaArvosanat():
    nimet = {}
    while True:
        nimi = input("Anna nimi: ")
        if nimi == "LOPPU":
            break
        else:
            try:
                arvosana = int(input("Anna arvosana: "))
            except:
                print("Virheellinen arvosana")
                continue
            if arvosana < 0:
                arvosana = 0
            elif arvosana > 5:
                arvosana = 5
            nimet[nimi] = arvosana
    return nimet


def TulostaHylatyt(nimet):
    for nimi in nimet:
        if nimet[nimi] == 0:
            print(nimi)


def PalautaHylattyjenMaara(nimet):
    hylatyt = 0
    for nimi in nimet:
        if nimet[nimi] == 0:
            hylatyt += 1

    print(hylatyt)
    return hylatyt


def TulostaKaikki(nimet):
    for nimi in nimet:
        print(nimi, nimet[nimi])


if __name__ == "__main__":
    # Write main program below this line
    nimet = LuoNimetJaArvosanat()
    hylatyt = TulostaHylatyt(nimet)
    hylatyt_maara = PalautaHylattyjenMaara(nimet)
    TulostaKaikki(nimet)
