#!/usr/bin/env python3

import math


def get_triangle_area(base, height):
	"""Return area of a triangle"""

	return (base * height ) / 2


def get_circle_area(r):
	"""Return area of a Circle"""

	return math.pi * (r ** 2)


if __name__ == '__main__':
	
	
	base = 5
	height = 10.55
	print(f"The rectangle area with base = {base} and height = {height} is: \n {get_triangle_area(base, height):.4}")
	
	radius = 4
	print(f"The circle area with radius {radius} is: \n {get_circle_area(radius):.4}")