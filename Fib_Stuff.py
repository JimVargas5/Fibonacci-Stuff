#Jim Vargas
#TODO: general sequence thing

import math
from Nth_Fib import Nth_Fib
from Sum_Nth_Fib import Sum_Nth_Fib
from Nth_Lucas import Nth_Lucas
from Sum_Nth_Lucas import Sum_Nth_Lucas

def check():
    print("Do you want to continue?")
    thing = input("Y or N?"+'\n'+">>> ")
    if (thing == "Y") or (thing == "y"):
        main()
    elif (thing == "N") or (thing == "n"):
        print("Quitting...")
        exit()
    elif len(thing) == 0:
        print("You didn't enter anything.")
        print("Quitting...")
        exit()
    elif len(thing) > 1:
        print("The program needs a one letter anser.", '\n')
        check()
    else:
        print("You entered something invalid.")
        print("Quitting...")
    exit()


def main():
    print("Wowee welcome to this Fibonacci mess of stuff.", '\n',
        "Type the corresponding number to pick what you want to do:", '\n',
        "0: quit", '\n',
        "1: return the nth number in the Fibonacci Sequence", '\n',
        "2: return the sum of the Fibonacci numbers up to the nth one", '\n',
        "3: return the nth number in the Lucas Sequence", '\n',
        "4: return the sum of the Lucas numbers up to the nth one", '\n'
        "That's all for now..."
     )
    which = input(">>> ")
    if which == "":
        print("You didn't enter anything you shmuck")
        check()
    elif which == "0":
        exit()
    elif which == "1":
        print("Which term in the sequence?")
        n = input(">>> ")
        try:
            int(n)
        except ValueError:
            print("You didn't enter a number you shmuck!")
            check()
        Nth_Fib(n,True)
    elif which == "2":
        print("Do you want to see the intermediate sums as it goes along?")
        steps = input("[y/n] >>> ")
        if steps == "y" or steps == "Y":
            print("Up to which term?")
            n = input(">>> ")
            try:
                int(n)
            except ValueError:
                print("You didn't enter a number you shmuck!")
                check()
            Sum_Nth_Fib(n,True,True)
        elif steps == "n" or steps == "N":
            print("Up to which term?")
            n = input(">>> ")
            try:
                int(n)
            except ValueError:
                print("You didn't enter a number you shmuck!")
                check()
            Sum_Nth_Fib(n,False,True)
        else:
            print("Enter 'y' or 'n' dammit!")
            check()
    elif which == "3":
        print("Which term in the sequence?")
        n = input(">>> ")
        try:
            int(n)
        except ValueError:
            print("You didn't enter a number you shmuck!")
            check()
        Nth_Lucas(n,True)
    elif which == "4":
        print("Do you want to see the intermediate sums as it goes along?")
        steps = input("[y/n] >>> ")
        if steps == "y" or steps == "Y":
            print("Up to which term?")
            n = input(">>> ")
            try:
                int(n)
            except ValueError:
                print("You didn't enter a number you shmuck!")
                check()
            Sum_Nth_Lucas(n,True,True)
        elif steps == "n" or steps == "N":
            print("Up to which term?")
            n = input(">>> ")
            try:
                int(n)
            except ValueError:
                print("You didn't enter a number you shmuck!")
                check()
            Sum_Nth_Lucas(n,False,True)
        else:
            print("Enter 'y' or 'n' dammit!")
            check()
    elif which == "poop":
        print("Bruh, you got the secret key! As a reward, this program will quit.")
        exit()
    else:
        print("You have to enter one of the number options!")
        check()


if __name__ == '__main__':
    main()