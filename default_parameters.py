#!/usr/bin/env python3


def greet(name, greeting="Hello"):
    print(greeting + ", " + name)


def get_triangle_area(base=2, height=10):
	"""Return area of a triangle"""

	return (base * height ) / 2


if __name__ == '__main__':

    # Call the function with default value
    greet("Armando")


    # Call the function with a custom greeting
    greet("Damaris", "Hi")


    # Call the function with default value
    print(f"The rectangle area with base = 2 and height = 10 is: \n {get_triangle_area():.4}")

    # Call the function with custom values
    base = 5
    height = 20
    print(f"The rectangle area with base = {base} and height = {height} is: \n {get_triangle_area(base, height):.4}")

    