"""
KT4

Tutustu omatoimisesti Pandas-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa.  Esimerkkisovellus on vapaavalintainen.


"""
# imports here
import pandas as pd


if __name__ == '__main__':
    # Main code here

    # Read data from csv file
    df = pd.read_csv('data/data.csv')
    print(df)

    # Edellä oleva lataa csv tiedoston Pandan dataframee ja tulostaa
    # Pythonilla voi analysoida isoa määrää dataa
    # Pandalla voi putsata sotkuista dataa ja tehdä siitä luettavaa
