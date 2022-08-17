

#iterating over dictionary.
from melons import melons


def print_melon(name):


    for i, j in melons.items():
        if name == i:
            print(name.upper())

    for a, b in j.items():
        print(f"{a}: {b}")


print_melon('Honeydew')

