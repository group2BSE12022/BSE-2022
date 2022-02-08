gd = input("Input Grade: ")
grade = float(gd)

def computegrade(grade):
    if 1 >= grade >= 0.0:
        if grade >= 0.9:
            print("A")
        elif grade >= 0.8:
            print("B")
        elif grade >= 0.7:
            print("C")
        elif grade >= 0.6:
            print("D")
        elif grade < 0.6:
            print("F")
    else:
        print("Bad Grade")

computegrade(grade)


