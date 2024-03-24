# INT , celi brojevi
# kalkulator

x = input("Prvi broj:")
y = input("Drugi broj:")

# int() pretvara input u int format
z = int(x) + int(y)

print(z)

#you can nest functions like this

i = int(input("treci broj:"))
n = int(input("cetvrti broj:"))


# can be done like this also

print(i + n)

# FLOAT , decimalni brojevi

i = float(input("decimale broj:"))
n = float(input("decimale broj:"))

# round , zaokruzi brojeve , , 2 znaci da zaokruzi na 2 decimale, ne mora se koristio opciono je

z = round(i + n, 2)
print(z)

# radi isto sto i z = round(i + n, 2) pomocu f stringa
print(f"{z:.2f}")
