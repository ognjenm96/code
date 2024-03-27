# using tuple, tuple is used to return multiple values from a function
# tuple is immutable, so it can't be changed
# tuple is defined by using () and values are separated by comma
# tuple can be accessed by index, e.g. tuple[0], tuple[1]
# tuple can be unpacked, e.g. name, house = get_student()

def main():
    student = get_student()
    print(f"Hello, {student[0]} from {student[1]}") #  student[0] is name and student[1] is house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)

if __name__ == "__main__":
    main()