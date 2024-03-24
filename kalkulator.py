def main():
    x = int(input("x je: "))
    print("Kvadrat od x:", kvadrat(x))

def kvadrat(n):
    return n + n # namerno menjam da ne radi kvadrat broja vec sabiranje da bi izazvali error

if __name__ == "__main__":
    main()