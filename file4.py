import csv

def save_student_info():
    """
    Saves student information to a CSV file.

    This function prompts the user to enter a name and a house,
    and then appends the information to a CSV file named "students.csv".
    The function also reads the contents of the CSV file and prints them.

    Args:
        None

    Returns:
        None
    """
    # Prompt the user to enter a name and a house
    ime = input("Unesite ime: ")
    kuca = input("Unesite kuću: ")

    # Append the information to the CSV file
    with open("students.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([ime, kuca])

    # Read the contents of the CSV file and print them
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=["Ime", "Kuća"])
        for row in reader:
            print(row)

# Call the function to save student information
save_student_info()
