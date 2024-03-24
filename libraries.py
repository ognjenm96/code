import random # ovo importuje random modul koji sadrazi odradjene funkcije

# na ovaj nacin impotujemo samo funkciju iz modula
from random import choice

# na ovaj nacin mozemo koristit funkciju direktno
dinar = choice(["par", "nepar"])
print(dinar)

novcic = random.choice(["glava", "pismo"]) # random je ovde modul a choice jedana od njegovih funkcija
print(novcic)

