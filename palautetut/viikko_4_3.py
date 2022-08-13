"""
KT3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden (liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet (0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60. 

Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:


KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina. 
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.

 
"""
# Write functions and define global variables here!
KR_PISTE = 90


def KysyHypynPituus():
    pituus = float(input("Anna hypyn pituus: "))
    return pituus


def KysyTuomareidenPisteet():
    tuomareiden_pisteet = []
    for i in range(5):
        pisteet = float(input("Anna tuomareiden pisteet: "))
        while pisteet < 0 or pisteet > 20:
            pisteet = float(input("Anna tuomareiden pisteet: "))
        tuomareiden_pisteet.append(pisteet)
    return tuomareiden_pisteet


def LaskeHypynPisteet(pituus, pisteet):
    jarjestettyPisteet = sorted(pisteet)
    kolmen_tuomarin_pisteet = jarjestettyPisteet[1:4]
    tulos = (pituus - KR_PISTE) * 1.8 + sum(kolmen_tuomarin_pisteet) + 60
    return int(tulos)


if __name__ == "__main__":
    # Write main program below this line
    pituus = KysyHypynPituus()
    tuomareiden_pisteet = KysyTuomareidenPisteet()
    pisteet = LaskeHypynPisteet(pituus, tuomareiden_pisteet)
    print(pituus)
    print(pisteet)
