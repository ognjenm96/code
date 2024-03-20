import random

def pogodi(x):
    random_number = random.randint(1, x)
    pogodi = 0
    while pogodi != random_number:
        pogodi = input(print(f'Pogodi izmedju 1 i {x}:'))
        if pogodi < random_number:
            print('Probaj veci broj')
        elif pogodi > random_number:
            print ('Probaj manji broj')
        else:
            print ('Bravo pogodi si!')