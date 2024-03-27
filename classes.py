class Ucenik: #klasa

    
def main():
    ucenik = get_ucenik()
    print(f"{ucenik.ime} iz {ucenik.skola}")

def get_ucenik():
    ucenik = Ucenik() #objekat klase, instanca klase
    ucenik.ime = input("Unesite ime ucenika: ")
    ucenik.skola = input("Unesite skolu ucenika: ")
    return ucenik

if __name__ == "__main__":
    main()