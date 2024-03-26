import re # import the regular expression module

email = input("Enter your email: ").strip()

# Check if the email is valid
# ^ means start of the string
# .+ means one or more of any character
# \w means any word character (a-z, A-Z, 0-9, _)
# \d means any digit (0-9)
# \s means any whitespace 
if re.search(r"^\w+@\w+\.\w", email): # The email must end with .rs
    print("Valid email")
else:
    print("Invalid email")