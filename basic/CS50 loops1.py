# for loops

for i in [0,1,2]: # [] pratstavlja listu, ovde sadrzi brojeve 0,1,2
    print("AV")

for n in range(3): # range(3) je funkcija odradjuje koliko puta ce se uraditi nesto
    print("meow")

for _ in range(3): # _ moze da se korisi kao varijabla 
    print("ahoj")  # koja samo naglasava da je tu varijabla 
                   # ali necemo menjati njenu vrednost
    
print("juhu\n" * 3, end="") # \n nam omogucuje da ispisemo na novim linijama
# end="" manje kraj da ne bude default \n vec praznina