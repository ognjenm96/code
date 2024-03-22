x = int(input("Unesi x: "))
y = int(input("Unesi y: "))

if x < y:
    print("x je manje od y")
elif x > y:
    print("x je vece od y")
else:
    print("x je jednako y")

if x < y or x > y: # if x != y postize isti rezultat kao sa or
    print("x nije jednako y")
else:
    print("x je jednako y")

broj_poena = int(input("Moj broj peana: "))

if broj_poena >= 90 and broj_poena <= 100:
    print("Ocena je 5!")
elif broj_poena >= 80 and broj_poena <=90:
    print("Ocena je 4!")
else:
    print("Ocena je manja od 4")

x =  int(input("Unesi broj: "))

if x % 2 == 0:
    print("paran broj")
else:
    print("neparan broj")

# funkcija za odradjevanje pranog i nepranog broja
def paran(n):
    if n % 2 == 0:
        return True
    else:
        return False