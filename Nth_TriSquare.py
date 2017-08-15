#Jim Vargas
#"A triangular number is the sum of the first so many positive integers. 
# For example, 10 is a triangular number because it equals 1+2+3+4. 
# These numbers are called triangle numbers because you can form a triangle 
# by having a row of one coin, two coin, three coins, etc. forming a triangle."
#Taken from: 
# https://www.johndcook.com/blog/2015/08/20/when-is-a-triangle-a-square/

import math

def Nth_TriSquare(n, square=False, p=False,):
    '''This function returns and can print the nth triangle 
        number that is also a square (z), starting at 1,36,... 
        It also uses the most explicit formula. More efficient functions
        can be written'''
    n = abs(int(n))
    z = (
            (
                (17 + 12*math.sqrt(2))**n + 
                (17 - 12*math.sqrt(2))**n - 2
            ) / 32
    )
    if square:
        if p:
            print("Nth square triangle number: ", round(z))
            print("Square of", str(round(z))+":", str(round(math.sqrt(z))))
        return round(z), round(math.sqrt(z))
    else:
        if p:
            print("Nth square triangle number: ", round(z))
        return round(z)

