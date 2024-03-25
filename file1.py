with open ("ucenici.csv") as file:
    for line in file:
        red = line.rstrip().split(",")
        print(f"{red[0]} je u {red[1]}")