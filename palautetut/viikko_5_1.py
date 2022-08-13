"""
KT1

Luontojärjestö KuopionBongarit tarvitsee uuden rekisterin, johon kaikki lintuhavainnot rekisteröidään.

Tee julkinen luokka Havainto, jolla on ominaisuudet:
- lintulaji, teksti
- maara, kokonaisluku, jos <0 muutetaan nollaksi
- tyyppi, teksti (Eli oliko lintu esim paikallinen vai muuttava)
- havaintopvm, datetime, ei voi olla tulevaisuuteen
- paikka, teksti
- kuvaus, teksti

Tee luokalle muodostin, jossa annetaan arvot kaikille luokan attribuuteille yllä olevassa järjestyksessä.
Tee kaikille jäsenmuuttujille getterit ja setterit Python-tekniikalla,  jotta tietoja pääsee muokkaamaan ja lukemaan. Tulosta getterissä viesti "getter" ja vastaavasti setterissä viesti "setter".
Tee myös __str__-metodi.
Testaa pääohjelmassa. Mitään sen kummempaa käyttöliittymää ei tarvitse tehdä. Riittää, että luot yhden Havainto olion ja tulostat sen tiedot hyödyntäen __str__ metodia.

"""
# Write class and imports here!
import datetime as dt


class Havainto:
    def __init__(self, lintulaji, maara, tyyppi, havaintopvm, paikka, kuvaus):
        self.lintulaji = lintulaji
        self.maara = maara
        self.tyyppi = tyyppi
        self.havaintopvm = havaintopvm
        self.paikka = paikka
        self.kuvaus = kuvaus

    @property
    def lintulaji(self):  # palauttaa arvon
        print("getter")
        return self._lintulaji

    @lintulaji.setter
    def lintulaji(self, value):  # sijoittaa arvon
        print("setter")
        self._lintulaji = value

    @property
    def maara(self):
        print("getter")
        return self._maara

    @maara.setter
    def maara(self, value):
        print("setter")
        if value < 0:
            value = 0
        self._maara = value

    @property
    def tyyppi(self):
        print("getter")
        return self._tyyppi

    @tyyppi.setter
    def tyyppi(self, value):
        print("setter")
        self._tyyppi = value

    @property
    def havaintopvm(self):
        print("getter")
        return self._havaintopvm

    @havaintopvm.setter
    def havaintopvm(self, value):
        print("setter")
        self._havaintopvm = value

    @property
    def paikka(self):
        print("getter")
        return self._paikka

    @paikka.setter
    def paikka(self, value):
        print("setter")
        self._paikka = value

    @property
    def kuvaus(self):
        print("getter")
        return self._kuvaus

    @kuvaus.setter
    def kuvaus(self, value):
        print("setter")
        self._kuvaus = value

    def __str__(self):
        return self.lintulaji + " " + str(self.maara) + " " + self.tyyppi + " " + str(self.havaintopvm) + " " + self.paikka + " " + self.kuvaus

    # def get_lintulaji(self):
    #     print("getter")
    #     return self.lintulaji

    # def set_lintulaji(self, lintulaji):
    #     print("setter")
    #     self.lintulaji = lintulaji

    # def get_maara(self):
    #     print("getter")
    #     return self.maara

    # def set_maara(self, maara):
    #     print("setter")
    #     self.maara = maara

    # def get_tyyppi(self):
    #     print("getter")
    #     return self.tyyppi

    # def set_tyyppi(self, tyyppi):
    #     print("setter")
    #     self.tyyppi = tyyppi

    # def get_havaintopvm(self):
    #     print("getter")
    #     return self.havaintopvm

    # def set_havaintopvm(self, havaintopvm):
    #     print("setter")
    #     self.havaintopvm = havaintopvm

    # def get_paikka(self):
    #     print("getter")
    #     return self.paikka

    # def set_paikka(self, paikka):
    #     print("setter")
    #     self.paikka = paikka

    # def get_kuvaus(self):
    #     print("getter")
    #     return self.kuvaus

    # def set_kuvaus(self, kuvaus):
    #     print("setter")
    #     self.kuvaus = kuvaus


if __name__ == "__main__":
    # Write main program below this line
    pvm = dt.datetime.now()
    strdate = pvm.strftime("%A")
    rekisteri = Havainto("Tikka", 5, "paikallinen", strdate,
                         "Tampere", "Upea ilmestys")
    print(rekisteri)
    # print(rekisteri.__str__())
    # print(rekisteri.get_paikka())
    # rekisteri.get_paikka()
    # rekisteri.set_paikka("Vantaa")
    # print(rekisteri.set_paikka("Helsinki"))
