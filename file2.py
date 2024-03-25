ucenici = []

with open("ucenici.csv") as file:
    for line in file:
        ime, skola = line.rstrip().split(",")
        ucenik = {}
        ucenik["ime"] = ime
        ucenik["skola"] = skola
        # ovako bi se bolje radilo
        # ucenik = {"ime": ime, "skola": skola}
        ucenici.append(ucenik)

def sortiraj_po_imenu(ucenik):
    return ucenik["ime"]

def sortiraj_po_skoli(ucenik):
    return ucenik["skola"]

for ucenik in sorted(ucenici, key=sortiraj_po_skoli):
    print(f"{ucenik['ime']} je u {ucenik['skola']}")