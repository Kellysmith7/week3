""""docstring that explains the program"""


def convert_inches_to_feet(inches):
    if inches > 0:
        feet = inches / 12
    else:
        feet = 0
    return int(feet)


def addition():
    x = input("Enter a number")
    y = input("Enter another number")
    return x + y



if __name__ == '__main__':
    print("Hello")
    print("28 inches is " + str(convert_inches_to_feet(28)) + " feet")
