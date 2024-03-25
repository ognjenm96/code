ime = input("Kako ti je ime? ")

file = open("ime.txt", "a")
file.write(ime)
file.close()