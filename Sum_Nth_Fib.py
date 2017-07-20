#Jim Vargas

import math
from Nth_Fib import Nth_Fib

def Sum_Nth_Fib(n, steps=False, p=False):
    '''This function returns and can print the sum of the Fibonacci numbers 
        up to the nth numberin the Fibonacci sequence (z), starting F(n=0) = 1.
        The input "steps" detemrines whether or not intermediate sums will
        be printed; the input "p" will determine if anything is printed.'''
    #NOTE: if steps==False and p==True, you shouldn't nest this function
        #in a print statement. 
    n = abs(int(n))
    z = 0
    if steps:
        for step in range(n+1):
            z += Nth_Fib(step)
            if step != n:
                if p:
                    print(("Step "+str(step)+":"), z)
        if p:
            print("Final sum:", z)
        return z
    else:
        for step in range(n+1):
            z += Nth_Fib(step)
        if p:
            print("Final sum:", z)
        return z


#print(Sum_Nth_Fib(0,True))
#print(Sum_Nth_Fib(2,True,True))
#print(Sum_Nth_Fib(2))
#print(Sum_Nth_Fib(2,False,True))
Sum_Nth_Fib(2,False,True)
            