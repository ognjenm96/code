print("Dobrodosli u kalkulator")

def operatori_brojeva():
    print("Moguce je uneti samo cele brojeve")
    x = int(input("Unesite prvi broj: "))
    i = str(input("Izaberite operaciju: +, -, *, / : "))
    y = int(input("Unesite drugi broj: "))
    zbir = x + y
    razlika = x - y
    proizvod = x * y
    kolicnik = x / y
    if i == '+':
        print(f"Zbir brojeva {x} i {y} je {zbir}")
    elif i == '-':
        print(f"Razlika brojeva {x} i {y} je {razlika}")
    elif i == '*':
        print(f"Proizvod brojeva {x} i {y} je {proizvod}")
    elif i == '/':
        print(f"Kolicnik brojeva {x} i {y} je {kolicnik}")
    else:
        print("Niste uneli validan broj")

operatori_brojeva()