import numpy as np


def important_function():
    hellos = []
    for hello in [np.array([1, 2, 3])] * 20:
        hellos.append(hello)
    return hellos


if __name__ == "__main__":
    print("This is a new feature which is awesome!")
    print("Another new feature implemented!")
    print("Something new")
    print("continue")
    hello_list = important_function()
    print(hello_list)
