'''
Write a program that does the following in order:
1. Asks the user to enter a number “x”
 2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
 4. Prints out the log (base 2) of “x”.
'''

import numpy
import math



if __name__ == "__main__":
    
    input_1 = int(input("type a number (x):"))
    input_2 = int(input("type another number (y):"))

    print(input_1, "to the power of", input_2, "=", input_1**(input_2))
    print("Log (base 2) of x is :", math.log2(input_1))