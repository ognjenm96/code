def main():
    meow(3)

def broj():
    while True:
        n = int(input("Broj : "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow!")

main()