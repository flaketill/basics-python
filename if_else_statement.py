#!/usr/bin/env python3


def get_odd_even():
    num = int(input("Please, enter a number: "))
    
    if num % 2 == 0:
        txt = "{0} is Even".format(num)
    else:
        txt = "{0} is Odd".format(num)
    
    return txt


if __name__ == '__main__':


    print(f"{get_odd_even()}")
    