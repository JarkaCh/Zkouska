#import tříd
from pojistenec import Pojistenec
from uvod import Uvod
uvod = Uvod()
pokracovat = True

#cyklus pro vypisování
while pokracovat:
    print(uvod.uvodni_strana())
    print(uvod.volby())
    vyber = int(input("Vyberte si číslo akce: "))

    # přidání pojištěnce
    if vyber == 1:
        Pojistenec.pridej_klienta(Pojistenec)
        input("Data byla uložena, pokračuj libovolnou klávesou... ")

    # vypsání všech pojištěných
    elif vyber == 2:
        Pojistenec.zobraz_seznam (Pojistenec)
        input("Pokračuj libovolnou klávesou... ")

    # vyhledání pojištěného
    elif vyber == 3:
        vyhledani = Pojistenec.vyhledavani(Pojistenec)
        if len(vyhledani) > 0:
            for pojistenec in vyhledani:
                print(pojistenec)
        else:
            print("Osoba nenalezena.")
        input("Pokračuj libovolnou klávesou... ")


    #konec
    elif vyber == 4:
        print("Děkujeme za použití naší aplikace.")
        pokracovat = False

