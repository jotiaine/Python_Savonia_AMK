"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:

LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän ja tallentaa tiedot dictionaryyn. Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU. Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022. Rekisteröintipäivämäärä pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt. Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot. Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
# Write functions, define global variables, and import modules here!

import datetime as dt


def LueAutot():
    cars = {}

    while True:
        plate = input("Syötä rekisterinumero : ")
        if plate.upper() == "LOPPU":
            break
        try:
            reg_date = dt.datetime.strptime(
                input("Syötä rekisteröintipäivämäärä : "), "%d.%m.%Y")
        except ValueError:
            print("Päivämäärä virheellinen")
        else:
            cars[plate] = reg_date

    return cars


def TalletaTiedostoon(cars_dict):
    filepath = "autot.txt"

    try:
        wfile = open(filepath, "wt")
        for key, value in cars_dict.items():
            wfile.write(key + "\t" + value.strftime("%d.%m.%Y") + "\n")
        wfile.close()
    except FileNotFoundError:
        print("Tiedostoa ei voitu avata")


def LueTiedostosta():
    filepath = "autot.txt"
    cars_info = {}

    try:
        rfile = open(filepath, "rt")
        line = rfile.readlines()
        for info in line:
            plate = info.split("\t")[0]
            reg_date = info.split("\t")[1].strip("\n")
            cars_info[plate] = reg_date
        rfile.close()
    except FileNotFoundError:
        print("Tiedostoa ei voitu avata")

    return cars_info


def TulostaTiedot(cars_dict):
    for key, value in cars_dict.items():
        print(key + "\t" + value)


if __name__ == "__main__":
    # Write main program below this line
    cars = LueAutot()
    TalletaTiedostoon(cars)
    cars_from_file = LueTiedostosta()
    TulostaTiedot(cars_from_file)
