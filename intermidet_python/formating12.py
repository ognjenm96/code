import re

url = input("Unesi URL: ").strip()

# re.sub - zamjenjuje dio stringa koji odgovara regularnom izrazu
# re.split - dijeli string na dijelove koji odgovaraju regularnom izrazu
# ^ - označava početak stringa
username = re.sub(r"^(https?://)?(www\.)?/(.+)", "", url)

print(f"Korisničko ime: {username}")