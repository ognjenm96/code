ucenici = ["Harry" , "Hermi", "Ron"]

print(ucenici[0]) # [broj] je index i ispisuje
# string po redu iz gore napravljene liste
# takodje broji od 0 sto je ovde Harry

# ova petlja ce ispisati sve iz gore napravljene liste
for ucenici in ucenici:
    print(ucenici)

for i in range(len(ucenici)): # prvi deo for petlje u ovom slucaju i je varijabla koju kreiramo u toj petlji
    print(ucenici[i])
    print (i + 1, ucenici[i]) # 