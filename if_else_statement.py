#!/usr/bin/env python3


def get_odd_even():
    num = int(input("Please, enter a number: "))
    
    if num % 2 == 0:
        txt = "{0} is Even".format(num)
    else:
        txt = "{0} is Odd".format(num)
    
    return txt

def get_grade_student():
    """
    Returns the grade based on the score the student received.

    Parameters:
    score (float): The score the student received. Must be between 0 and 100.

    Returns:
    str: The grade the student received, based on the following scale:
        Score >= 90: "A"
        Score >= 80: "B"
        Score >= 70: "C"
        Score >= 60: "D"
        Score < 60: "F"
    """


    grade = int(input("\n Please, enter your grade (10,55,90,100, etc): "))

    
    if grade >= 90:        
        msn = "You have an A."
    elif grade >= 80:
        msn = "You have a B."
    elif grade >= 70:
        msn = "You have a C."
    elif grade >= 60:
        msn = "You have a D."
    else:
        msn = "You have an F."        
    
    
    return msn    


if __name__ == '__main__':


    print(f"{get_odd_even()}")

    print(f"\n {get_grade_student()}")
