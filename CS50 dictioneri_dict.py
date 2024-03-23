# Dictionary , dict, key values pair

ucenici = ["Harry" , "Hermi", "Ron"]
kuce = ["Grifindor", "Sliterin" , "Honypof"]

studenti = {
    "Hary": "Grifindor",
    "Hermi": "Hofpof",
    "Drako": "Sliterin"
    # key : # value ,
} # {} zagradama se pravi dictionery

print(studenti["Hary"]) # dictioneri dozvoljava da se koristi ime iz dict kao value
print(studenti["Drako"]) # dobijemo iz koje su kuce jer je to njegov par

# ova petlja ce ispirsati key i value par
for student in studenti:
    print(student, studenti[student])