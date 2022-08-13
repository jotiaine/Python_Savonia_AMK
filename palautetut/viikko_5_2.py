"""
KT2


Olet aloittanut osakesijoittamisen ja haluat arvioida sijoituksesi arvoa. Ohjelmalla (pääohjelmassa) on lista, johon käyttäjä voi lisätä Osake-olioita. Ohjelma kysyy käyttäjältä ”Lisätäänkö uusi osake (k/e)”.
Kun osakkeet on lisätty listaan, kysyy ohjelma käyttäjältä kuvitteellisen kasvuprosentin sekä ajanjakson vuosina.


Tee luokka Osake, jolla on jäsenmuuttujat:
- nimi
- ostohinta (>0, osakekohtainen ostohinta)
- maara (> 0, omistettujen osakkeiden lkm)



Osakkeella on metodit:

- tulosta_arvo, jonka parametreina on  kasvuprosentin ja ajanjakson vuosina (tässä järjestyksessä). tulosta_arvo-metodi kutsuu toista Osake-luokan  metodia laske_tuotto_yhdelle_vuodelle, joka laskee vuosikohtaisen tuoton. tulosta_arvo kutsuu laske_tuotto_yhdelle_vuodelle-metodia vuosien lukumäärän verran. Siis, jos lasketaan tuottoa kolmelle vuodelle, niin laske_tuotto_yhdelle_vuodelle kutsutaan kolme kertaa. Huomio "korkoa korolle". Valuutat tulostetaan kahden desimaalin tarkkuudella.

- laske_tuotto_yhdelle_vuodelle -metodi palauttaa tuoton yhdelle vuodelle. Metodi on staattinen ja saa parametrinaan kasvuprosentin ja hinnan vuoden alussa (tässä järjesyksessä).

Laske pääohjelmassa  myös koko osakepotin arvo(sama % ja samat vuodet) käymällä lista läpi eli 
joudut miettimään sitä, miten pääohjelmaan palautetaan tieto yhden osakkeen potin arvosta vuosien jälkeen.

Esimerkkiajo:


Anna osakkeen nimi: Nokia
Anna osakkeen ostohinta/kpl: 10
Anna ostettujen osakkeiden lukumäärä: 1000
Lisää osakkeita (k/e)? k

Anna osakkeen nimi: Fortum
Anna osakkeen ostohinta/kpl: 12
Anna ostettujen osakkeiden lukumäärä: 127
Lisää osakkeita (k/e)? e

Anna kasvuprosentti: 5
Anna vuodet: 3

Nokia 1000 10.0
Osakkeen potin arvo on 11576.25 ja tuotto 1576.25

Fortum 127 12.0
Osakkeen potin arvo on 1764.22 ja tuotto 240.22

Koko potin arvo on 13340.47
"""
# Write class and imports here!


class Osake:
    def __init__(self, nimi, ostohinta, maara):
        self.nimi = nimi
        self.ostohinta = ostohinta
        self.maara = maara

    @property
    def nimi(self):
        return self._nimi

    @property.setter
    def nimi(self, value):
        self._nimi = value

    @property
    def ostohinta(self):
        return self._ostohinta

    @property.setter
    def ostohinta(self, value):
        self._ostohinta = value

    @property
    def maara(self):
        return self._maara

    @property.setter
    def maara(self, value):
        self._maara = value

    def tulosta_arvo(self, kasvuprosentti, ajanjakso):
        tuotto = self.maara * self._ostohinta
        korko = 0.0
        counter = 0
        while counter < ajanjakso:
            tuottovuodelle = Osake.laske_tuotto_yhdelle_vuodelle(
                kasvuprosentti, tuotto)
            tuotto += tuottovuodelle
            korko += tuottovuodelle
            counter += 1
        return korko

    def laske_tuotto_yhdelle_vuodelle(kasvuprosentti, hinta):
        prosentti = kasvuprosentti * 0.01 + 1
        korko_vuodelle = (hinta * prosentti) - hinta
        return korko_vuodelle


if __name__ == "__main__":
    # Write main program here
    osakkeet = list()

    lisataanko = "k"

    while lisataanko == "k" or lisataanko == "K":
        nimi = input("Anna osakkeen nimi: ")
        ostohinta = float(input("Anna osakkeen ostohinta / kpl: "))
        maara = int(input("Anna ostettujen osakkeiden lukumäärä: "))
        osakkeet.append(Osake(nimi, ostohinta, maara))
        lisataanko = input("Lisää osakkeita (k/e)? ")

    kasvuprosentti = float(input("Anna kasvuprosentti: "))
    vuodet = int(input("Anna vuodet: "))

    kokopotti = 0

    for osake in osakkeet:
        print("{}{}{}".format(osake.nimi, osake.maara, osake.ostohinta))
        tuottoprint = (osake.tulosta_arvo(kasvuprosentti, vuodet))
        arvo = (osake.maara * osake.ostohinta) + tuottoprint
        print("Osakkeen potin arvo on {:.2f} ja tuotto {:.2f}".format(
            arvo, tuottoprint))
        kokopotti += arvo

    print("Koko potin arvo on {0}".format(kokopotti))
