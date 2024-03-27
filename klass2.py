class Ucenik:
    def __init__(self, ime, skola): 
        if not ime:
            raise ValueError("Ime ne sme biti prazno")
        if skola not in ["Masinska", "Gimnazija", "Tehnicka","Ekonomska"]:
            raise ValueError("Skola nije validna")
        self.ime = ime 
        self.skola = skola

    def __str__(self):
        return f"{self.ime} pohadja {self.skola}"
    
    # property in python is a special decorator that allows us to define a method but we can access it like an attribute

    # Getter is a method that gets the value of a specific attribute
    @property # getter
    def skola(self):
        return self._skola # _skola is a private attribute
    
    # Setter is a method that sets the value of a specific attribute
    @skola.setter # setter
    def skola(self, skola):
        if skola not in ["Masinska", "Gimnazija", "Tehnicka","Ekonomska"]:
            raise ValueError("Skola nije validna")
        self._skola = skola # _skola is a private attribute
    
def main():
    ucenik = get_ucenik()
    print(ucenik)
    
def get_ucenik():
    ime = input("Unesite ime ucenika: ")
    skola = input("Unesite skolu ucenika: ") 
    return Ucenik(ime, skola) 

if __name__ == "__main__": 
    main()