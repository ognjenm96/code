import random

def pogodi(broj):
    random_number = random.randint(1, broj)
    pogodi = 0
    while pogodi != random_number:
        pogodi = int(input((f'Pogodi izmedju 1 i {broj}:')))
        if pogodi < random_number:
            print('Probaj veci broj')
        elif pogodi > random_number:
            print('Probaj manji broj')
        else:
            print('Bravo pogodi si!')