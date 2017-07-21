#Jim Vargas

import math
from Nth_Lucas import Nth_Lucas

def Sum_Nth_Lucas(n, steps=False, p=False):
    '''This function returns and can print the sum of the Lucas numbers 
        up to the nth number in the Lucas sequence (z), starting L(n=0) = 2,
        L(n=1) = 1.The input "steps" detemrines whether or not intermediate 
        sums will be printed; the input "p" will determine if anything is printed.'''
    #NOTE: if steps==False and p==True, you shouldn't nest this function
        #in a print statement. 
    n = abs(int(n))
    z = 0
    if steps:
        for step in range(n+1):
            z += Nth_Lucas(step)
            if step != n:
                if p:
                    print(("Step "+str(step)+":"), z)
        if p:
            print("Final sum:", z)
        return z
    else:
        for step in range(n+1):
            z += Nth_Lucas(step)
        if p:
            print("Final sum:", z)
        return z