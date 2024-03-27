class Ucenik: #klasa
    # atributi klase (promenljive) - karakteristike objekta
    def __init__(self, ime, skola, predmet): # konstruktor klase (inicijalizacija)
        if not ime:
            # izbacujemo izuzetak ako je ime prazno
            # raise - izbacuje izuzetak, ValueError - tip izuzetka 
            raise ValueError("Ime ne sme biti prazno")
        if skola not in ["Masinska", "Gimnazija", "Tehnicka","Ekonomska"]:
            raise ValueError("Skola nije validna")
        self.ime = ime # atributi klase
        self.skola = skola # atributi klase
        self.predmet = predmet

    def __str__(self): # metoda klase, koja vraca string
        # f-string - formatiranje stringa
        # metoda klase
        return f"{self.ime} pohadja {self.skola} i uci {self.predmet}"
    
    def predmeti(self):
        match self.predmet:
            case "Matematika":
                return "2+2=4"
            case "Fizika":
                return "Formula za brzinu je v=s/t"
    
def main():
    ucenik = get_ucenik()
    print(ucenik) # pristupamo metodi klase
    print(ucenik.predmeti()) # pristupamo metodi klase
    
def get_ucenik():
    ime = input("Unesite ime ucenika: ") # atributi klase
    skola = input("Unesite skolu ucenika: ") # atributi klase
    predmet = input("Unesite predmet ucenika: ")
    return Ucenik(ime, skola, predmet) # kreiranje objekta klase

if __name__ == "__main__": # provera da li je fajl pokrenut direktno
    main()