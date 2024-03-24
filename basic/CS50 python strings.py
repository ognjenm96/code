# VARIABLES AND STRINGS

# = je operator dodele == znaci jednako za pogram
# using user input, by default input is expecting string input
name = input("Your name ? ") 
# printing user input
print("Hello, ", name)  
# \ eskejp karakter
print("\"")
# f string , formatira text i koristi se uz {} zagrade
print(f"Moje ime:{name}")
# Neke funkcije se mogu koristiti uz str , pogledaj dokumentaciju svih koje postoje
# primer, ova brise whitespace iz str i dodaje velika slova gde je potrebno
# FUnkcije se mogu dodavati lancano jedna na drugu
name = name.strip().title()
print(name)
# mozemo koristiti i ovako da postignemo isto
name = input("Your name ? ").strip().title()
print(name)

# Python can be use interactiv (interactiv mode), just type python or python3 on the terminal
