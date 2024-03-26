import re

def format_imena():
    ime_unos = input("Unesi ime: ").strip()
    if "." in ime:
        ime, prezime = ime_unos.split(". ")
        ime_unos = f"{ime} {prezime}"
    print(f"Zdravo: {ime}")

def formatiranje1():
    unos_imena = input("Unesi imee: ").strip()
    # jos jedan nacin na koji moze isto da se uradi
    # if frmatiranje_imena := re.search(r"^.+, .+$", unos_imena)
    # unos_imena = formatiranje_imena.group(2) + " " + formatiranje_imena.group(1)
    frmatiranje_imena = re.search(r"^.+, .+$", unos_imena)
    if frmatiranje_imena:
        ime , prezime = frmatiranje_imena.groups()
        unos_imena = f"{ime} {prezime}"
    # moze se uraditi i ovako
    # prezime = formatiranje_imena.group(1)
    # ime = formatiranje_imena.group(2)
    # ili ovako unos_imena = formatiranje_imena.group(2) + " " + formatiranje_imena.group(1)
    print(f"Zdravo: {unos_imena}")

# := je walrus operator koji se koristi za dodelu vrednosti promenljivoj i istovremeno koriscenje te vrednosti

formatiranje1()