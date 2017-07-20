#Jim Vargas
import math

def Nth_Fib(n,p=False):
    '''This function returns the nth number in the Fibonacci sequence (z), 
        starting F(n=0) = 1'''
    n = abs(int(n))
    z = (
            (1/math.sqrt(5)) * (
                ( (1+math.sqrt(5) ) / 2) ** (n+1)) - 
            (1/math.sqrt(5)) * (
                ( (1-math.sqrt(5) ) / 2) ** (n+1))
    )
    if p:
        print("Nth term:", round(z))
    return round(z)


#print(Nth_Fib(0))
#print(Nth_Fib(1))
#print(Nth_Fib(3))
#print(Nth_Fib(19))
