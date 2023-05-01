#!/usr/bin/env python3


def get_odd_even():
    """ Return if an integer is even or odd"""

    
    num = int(input("Please, enter a number: "))

    msn = f"{num} is even" if num % 2 == 0 else f"{num} is odd"
    
    return msn


def check_list():
    
    
    list_example = [1, 2, 3]
    
    result = "The list is Non empty" if list_example else "he list is empty"

    return result

if __name__ == '__main__':


    print(f"{get_odd_even()}")


    print(f"{check_list()}")
