#!/usr/bin/env python3


def greet(name, greeting="Hello"):
    print(greeting + ", " + name)


if __name__ == '__main__':

    # Call the function with default value
    greet("Armando")


    # Call the function with a custom greeting
    greet("Damaris", "Hi")
    