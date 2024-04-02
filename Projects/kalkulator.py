def main():
    print("Moguce je uneti samo cele brojeve")

def operatori_brojeva(i):
    x = int(input("Unesite prvi broj: "))
    z = int(input("Izaberite operaciju: +, -, *, /"))
    y = int(input("Unesite drugi broj: "))
    zbir = x, z, y
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
    
if __name__ == main():
    operatori_brojeva(i)
    main()