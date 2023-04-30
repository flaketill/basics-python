#!/usr/bin/env python3


def greet(name, greeting="Hello"):
    print(greeting + ", " + name)


def get_triangle_area(base=2, height=10):
	"""Return area of a triangle"""

	return (base * height ) / 2


def get_price_after_discount(price, discount_in_percentage):
    """Return final price when apply a discount, The default discount rate is 5%"""
    if discount_in_percentage == None:
        discount_in_percentage = 5
    
    return price - (price * (discount_in_percentage / 100))


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

    price = 1000
    print(f"The final Price of {price} after discount (dafault 5%):  \n {get_price_after_discount(price, None)}")


    price = 125
    discount = 25
    print(f"The final Price of {price} after discount:  \n {get_price_after_discount(price, discount)}")

    