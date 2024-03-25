import csv

ucenik = []

with open('ucenici.csv') as file:
    reader = csv.reader(file)
    for ime, skola in reader:
        ucenik.append({"ime": ime, "skola": skola})

for ucenik in sorted(ucenik, key=lambda ucenik: ucenik["skola"]):
    print(f"{ucenik['ime']} je u {ucenik['skola']}")