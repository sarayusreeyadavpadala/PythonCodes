
#This Python code calculates the factorial of a number given by the user.

import sys


def Factorial(num):
#This function calculates the factorial of a number.
    mul = 1
    for i in range(0,num):
        if num == 0: #If the input which was given by the user is Zero,It returns One.
            return 1
        else:
            mul = mul*(num-i) #Else it will calculate the factorial of the number.
    return mul
    
def get_input():
#This function gets an integer input from the user.If it was not an integer it gives three chances to the user to give a right input.
    for i in range(3,0,-1):                      
        num = input("enter a number:")
        if num.isnumeric():  #checks if input is numeric using .isnumeric().                 
            num = int(num)                      
            return num
        else:
            print("enter integer only")                    
            print(f'{i-1} chances are left' if (i-1)>1 else f'{i-1} chance is left') 
        continue   

if __name__ == '__main__':
    num = get_input()
    if type(num) is type(None):               
        print("Try again!")
        sys.exit()
    else:
        fact=Factorial(num)
        print(f'The factorial of {num} is {fact}')
