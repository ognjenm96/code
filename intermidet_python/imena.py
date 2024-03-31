def save_name():
    """
    This function prompts the user to enter their name and saves it to a file called "ime.txt".
    """

    # Prompt the user to enter their name
    ime = input("Kako ti je ime? ")

    # Open the file in append mode and write the name to it
    with open("ime.txt", "a") as file:
        file.write(f"{ime}\n")
