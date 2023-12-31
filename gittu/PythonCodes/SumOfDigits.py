# Python code to calculate the sum of digits of a number, by taking number input from user.

import sys

def get_integer():
    """ This function asks the user to give the input. It gives 3 chances until user enter the correct
    number """

    for i in range(3,0,-1):                       # executes the loop 3 times. Giving 3 chances to the user.
        num = input("enter a number:")
        if num.isnumeric():                       # checks if entered input is an integer string or not.
            num = int(num)                        # converting integer string to integer. And returns it to where function is called.
            return num
        else:
            print(f'{i-1} chance is left' if (i-1)<2 else f'{i-1} chances are left')   # printing no of chances left

        continue   


def addition(num):
    """ This function performs addition. If user enters wrong value, program exits """

    Sum=0
    if type(num) is type(None):               # Checks if number type is none or not. If type is none program exits.
        print("Try again!")
        sys.exit()
    while num > 0:                            # Addition- adding the digits in the number.
        digit = int(num % 10)
        Sum += digit
        num /= 10
    return Sum                                # Returns sum to where the function is called.




if __name__ == '__main__':                    
    """ This function is used to overcome the problems while importing this file """                        
    number = get_integer()
    Sum = addition(number)
    print(f'Sum of digits of {number} is {Sum}')      # Prints the sum

