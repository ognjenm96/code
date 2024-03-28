class Sef:
    def __init__(self, zlato=0, srebro=0, bakar=0):
        self.zlato = zlato
        self.srebro = srebro
        self.bakar = bakar
    
    def __str__(self):
        return f"Zlato: {self.zlato}, Srebro: {self.srebro}, Bakar: {self.bakar}"

    # Overloading the + operator
    def __add__(self, other):
        zlato = self.zlato + other.zlato
        srebro = self.srebro + other.srebro
        bakar = self.bakar + other.bakar
        return Sef(zlato, srebro, bakar)

potter = Sef(100, 200, 300)
print(potter)

weasley = Sef(50, 15, 5)
print(weasley)

# Overloading the + operator
total = potter + weasley
print(total)