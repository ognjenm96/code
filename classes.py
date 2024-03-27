class Ucenik: #klasa
    # atributi klase (promenljive) - karakteristike objekta
    def __init__(self, ime, skola): # konstruktor klase (inicijalizacija)
        if not ime:
            # izbacujemo izuzetak ako je ime prazno
            # raise - izbacuje izuzetak, ValueError - tip izuzetka 
            raise ValueError("Ime ne sme biti prazno")
        if skola not in ["Masinksa", "Gimnazija", "Tehnicka","Ekonomska"]:
            raise ValueError("Skola nije validna")
        self.ime = ime # atributi klase
        self.skola = skola # atributi klase

    
def main():
    ucenik = get_ucenik()
    print(f"{ucenik.ime} iz {ucenik.skola}") #pristupamo atributima klase

def get_ucenik():
    ime = input("Unesite ime ucenika: ") # atributi klase
    skola = input("Unesite skolu ucenika: ") # atributi klase
    return Ucenik(ime, skola) # kreiranje objekta klase

if __name__ == "__main__":
    main()