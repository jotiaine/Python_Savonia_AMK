"""
KT1


Tee ohjelma, jossa kysytään KysyJaTestaaLuku() nimisessä funktiossa  käyttäjältä kokonaisluku. 

Funktio palauttaa kokonaislukuarvon seuraavasti:

 

1, jos syötetty luku on positiivinen.
0, jos syötetty luku on nolla.

-1, jos syötetty luku on negatiivinen. 

 

Tulosta näiden paluuarvojen perusteella pääohjelmassa ilmoitus ruudulle.


”Luku oli positiivinen”, jos paluuarvo oli 1.
”Luku oli nolla”, jos paluuarvo oli 0
”Luku oli negatiivinen”, jos paluuarvo oli -1.

"""

# Write KysyJaTestaaLuku function here!


def KysyJaTestaaLuku():
    kokonaisluku = int(input("Anna kokonaisluku: "))

    if kokonaisluku > 0:
        kokonaisluku = 1
    elif kokonaisluku == 0:
        kokonaisluku = 0
    else:
        kokonaisluku = -1

    return kokonaisluku


if __name__ == "__main__":
    # Write main program below this line

    def tulostus():
        kokonaisluku = KysyJaTestaaLuku()

        if kokonaisluku == 1:
            print("Luku oli positiivinen")
        elif kokonaisluku == 0:
            print("Luku oli nolla")
        else:
            print("Luku oli negatiivinen")

    tulostus()
