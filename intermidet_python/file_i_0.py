imena = []

for i in range(3):
    ime = input("Ime? ")
    imena.append(ime)

for ime in sorted(imena):
    print(f"zdravo, {ime}")