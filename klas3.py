class Ucenik:
    def __init__(self, ime, skola): 
        self.ime = ime 
        self.skola = skola

    def __str__(self):
        return f"{self.ime} pohadja {self.skola}"
    
    @classmethod # metoda klase
    def get(cls):
        ime = input("Unesite ime ucenika: ")
        skola = input("Unesite skolu ucenika: ")
        return cls(ime, skola)
    
def main():
    ucenik = Ucenik.get()
    print(ucenik)

if __name__ == "__main__": 
    main()