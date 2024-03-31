class Hat:
    # house is a class variable that is shared among all instances of a this class
    house = ["Gryffindor, Hufflepuff, Ravenclaw, Slytherin"]

    # @staticmethod is a decorator that defines a method that is bound to the class, not the instance of the class
    @staticmethod
    def sort(cls, name):
        # random.choice() returns a random element from the non-empty sequence
        print(ime, "is in" , random.choice(cls.house))

# create an instance of the Hat class
Hat.sort("Harry")
              