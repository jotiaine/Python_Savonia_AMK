"""
KT3

Tutustu omatoimisesti NymPy-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa. Esimerkkisovellus on vapaavalintainen.



"""
# imports here
import numpy as np

if __name__ == '__main__':
    # Main code here
    numerot = [0.25123, 0.56345, 0.75234, 1.2234,
               1.5325, 1.75435]
    print("Annetut numerot: \n", numerot)

    pyoristys = np.round_(numerot)
    print("\nPyöristetyt numerot: \n", pyoristys)
