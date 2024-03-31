def print_names_from_file():
    """
    Reads a file named 'ime.txt' and prints each line with 'hello' prefix.

    Args:
        None

    Returns:
        None
    """
    # Open the file in read mode
    with open("ime.txt", "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Print the line with 'hello' prefix
            print("hello", line.strip())

# Call the function to execute the code
print_names_from_file()