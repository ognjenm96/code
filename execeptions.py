# try se koristi da se proba kod ispod njega
try:
    x = input(") # ovde postoji SyntaxError
    print()
# except se koristi da odradi nesto ako nesto krene po zlu da ispise to
except SyntaxError:
    print(SystemError) # ovde ispise koji je SynaxError