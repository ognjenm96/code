import csv
# Create an empty list to store the student information
ucenici = []

# Open the "ucenici.csv" file
with open("ucenici.csv") as file:
    # Read each line in the file
    for line in file:
        # Split the line by comma and remove any trailing whitespace
        ime, skola = line.rstrip().split(",")

        # Create a dictionary to store the student's name and school
        ucenik = {}
        ucenik["ime"] = ime
        ucenik["skola"] = skola

        # Add the student dictionary to the list
        ucenici.append(ucenik)

def sortiraj_po_imenu(ucenik):
    """Sorts the student dictionary by name."""
    return ucenik["ime"]

def sortiraj_po_skoli(ucenik):
    """Sorts the student dictionary by school."""
    return ucenik["skola"]

# Sort the list of students by school using the sortiraj_po_skoli function as the key
for ucenik in sorted(ucenici, key=sortiraj_po_skoli):
    # Print the student's name and school
    print(f"{ucenik['ime']} je u {ucenik['skola']}")