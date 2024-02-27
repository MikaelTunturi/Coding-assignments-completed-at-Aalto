'''
@author: mikaeltunturi
'''

def to_metric():
    feet = int(input("How tall are you (in feet)?\n"))
    inches = int(input("And how many inches on top of that?\n"))
    total_cm = (feet * 12 + inches) * 2.54
    print("You are {:.0f} centimetres tall.".format(total_cm))
    
def to_imperial():
    cm = int(input("How tall are you in centimetres?\n"))
    feet = cm // (12 * 2.54)
    inches = (cm / 2.54) - (feet * 12)
    print("You are", int(feet), "feet and", int(inches), "inches tall.")
    
def main():
    print("1. Convert from the metric system")
    print("2. Convert to the metric system")
    print("3. End")
    choice = int(input("What do you want to do?\n"))
    while choice != 3:
        if choice == 2:
            to_metric()
        elif choice == 1:
            to_imperial()
        print("Do you want to continue?")
        print("1. Convert from the metric system")
        print("2. Convert to the metric system")
        print("3. End")
        choice = int(input("What do you want to do?\n"))
    print("Program terminating.")

main()
