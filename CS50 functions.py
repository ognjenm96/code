# DEF , pravi funkciju koju sami kreiramo i definisemo

def main():
    name = input("Ime ? ")
    # ovde smo pozvali hello funkciju i ova izvrsava kod koji je dole napisan u okviru hello funkcije
    hello(name) 

# ovde je hello funkcija 
def hello(to):
    # ovde se nalazi kod koji se izvrsava u okviru hello funkcije
    print("hello", to) 

# da bi ostale funkcije radile na kraju programa moramo pozvati main funkciju
main()