import random # ovo importuje random modul koji sadrazi odradjene funkcije

# na ovaj nacin impotujemo samo funkciju iz modula
from random import choice

# na ovaj nacin mozemo koristit funkciju direktno
dinar = choice(["par", "nepar"])
print(dinar)

novcic = random.choice(["glava", "pismo"]) # random je ovde modul a choice jedana od njegovih funkcija
print(novcic)

# randint daje randombroj u okviru koji mu postaimo ovde, 1 do 10
broj = random.randint(1, 10)
print(broj)

# ova funkcija mesa raspored iz lisste i printa ih
karte = ["kralj", "kraljica", "dzoker", "as"]
random.shuffle(karte)
for karta in karte:
    print(karta)
