import re

def find_emails(text):
    """
    Find all email addresses in the given text using regular expressions.

    Args:
        text (str): The text to search for email addresses.

    Returns:
        list: A list of email addresses found in the text.
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    # Find all matches of the email pattern in the text
    matches = re.findall(email_pattern, text)

    # Print each match
    for match in matches:
        print(match)

    # Return the list of matches
    return matches

# Example usage
text = "Please contact me at john.doe@example.com or jane_smith@example.co.uk"
find_emails(text)
