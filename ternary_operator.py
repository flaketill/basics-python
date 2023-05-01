#!/usr/bin/env python3


def get_odd_even():
    """ Return if an integer is even or odd"""

    
    num = int(input("Please, enter a number: "))

    msn = f"{num} is even" if num % 2 == 0 else f"{num} is odd"
    
    return msn


if __name__ == '__main__':


    print(f"{get_odd_even()}")
