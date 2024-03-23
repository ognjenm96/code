while True:
    n = int(input("Koliko je n: "))
    if n < 0:
        continue
    else:
        break
# simple and better way is 
# while True:
#     n = int(input("Koliko je n: "))
#     if n > 0:
#         break
for _ in range(n):
    print("meow!")