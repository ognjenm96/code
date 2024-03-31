import re # import the regular expression module

email = input("Enter your email: ").strip()

# Check if the email is valid
# ^ means start of the string
# + means one or more of the preceding character
# .+ means one or more of any character
# ? means zero or one of the preceding character
# () means a group of characters
# [a-zA-Z0-9] means any letter or digit
# \w means any word character (a-z, A-Z, 0-9, _)
# \d means any digit (0-9)
# \s means any whitespace 
# re.IGNORECASE means ignore the case of the characters
# re.MULTILINE means the string is multi-line
# re.DOTALL means the dot (.) will match any character, including a newline
# re.fullmatch() means the entire string must match the pattern

if re.search(r"^\w+@(\w\.)?\w+\.\w", email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")