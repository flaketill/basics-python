#!/usr/bin/env python3

import math


def get_triangle_area(base, height):
	"""Return area of a triangle"""

	return (base * height ) / 2


if __name__ == '__main__':
	
	
	base = 5
	height = 10.55
	print(f"The rectangle area with base = {base} and height = {height} is: \n {get_triangle_area(base, height):.4}")