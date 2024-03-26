import re # import the regular expression module

email = input("Enter your email: ").strip()

# Check if the email is valid
if re.search("..*@.*", email):
    print("Valid email")
else:
    print("Invalid email")