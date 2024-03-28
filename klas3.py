class Ucenik:
    def __init__(self, ime, skola): 
        self.ime = ime 
        self.skola = skola

    def __str__(self):
        return f"{self.ime} pohadja {self.skola}"
    
def main():
    ucenik = get_ucenik()
    print(ucenik)
    
def get_ucenik():
    ime = input("Unesite ime ucenika: ")
    skola = input("Unesite skolu ucenika: ") 
    return Ucenik(ime, skola) 

if __name__ == "__main__": 
    main()