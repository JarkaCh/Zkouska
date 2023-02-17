class Pojistenec:

    def __init__(self, jmeno, prijmeni, tel_cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.cislo = tel_cislo
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno}, {self.prijmeni}, {self.cislo}, {self.vek}"

    #přidání nového klienta

    def pridej_klienta(self):
        new_jmeno = str(input("Zadejte jméno pojištěného:\n"))
        new_prijmeni = str(input("Zadejte příjmení:\n"))
        new_cislo = str(input("Zadejte telefonní číslo:\n"))
        while len(str(new_cislo)) !=9:
            print("Chybný formát čísla.")
            new_cislo = str(input("Zadejte znovu devítimístné tel. číslo:\n"))
        new_vek = str(input("Zadejte věk:\n"))

    # výpis všech pojištěných

    def zobraz_seznam(self):
        for pojistenec in pojistenci: print(pojistenec)

    # vyhledávání pojištěného

    def vyhledavani(self):
        vyhledej_jmeno = input("Napiš jméno: ")
        vyhledej_prijmeni = input("Napiš příjmení: ")
        vysledek_hledani = []
        for pojistenec in pojistenci:
            if pojistenec.jmeno == vyhledej_jmeno and pojistenec.prijmeni == vyhledej_prijmeni:
                vysledek_hledani.append(pojistenec)
        return vysledek_hledani

    # fiktivní pojištěnci
pojistenci = []
pavel = Pojistenec("Pavel", "Novotný", "724632019", "27")
jana = Pojistenec("Jana", "Tichá", "721590385", "40")
daniel = Pojistenec("Daniel", "Zoubek", "254031719","50")
pojistenci.append(pavel)
pojistenci.append(jana)
pojistenci.append(daniel)

