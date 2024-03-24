def main():
    print_stub(4) # ovde dajemo funkciji ranger koliko puta ce ispisati #
   
def print_stub(kocka):
    for i in range(kocka):
        for n in range(kocka):
            print("#" , end=" ")
        print()
    
main()