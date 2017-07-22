#Jim Vargas
import math

def Nth_Lucas(n,p=False):
    '''This function returns and can print the nth number in the 
        Lucas sequence (z), starting L(n=0) = 2, L(n=1) = 1'''
    n = abs(int(n))
    z = (
        ( (1+math.sqrt(5) ) / 2) ** (n) + 
        ( (1-math.sqrt(5) ) / 2) ** (n)
    )
    if p:
        print("Nth term:", round(z))
    return round(z)


#Nth_Lucas(0,True)
#Nth_Lucas(1,True)
#Nth_Lucas(36,True)