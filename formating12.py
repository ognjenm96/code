import re

url = input("Unesi URL: ").strip()

# re.sub - zamjenjuje dio stringa koji odgovara regularnom izrazu

username = re.sub(r"https://", "", url)

print(f"Korisničko ime: {username}")