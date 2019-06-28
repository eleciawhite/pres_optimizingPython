#!/usr/bin/env python3
# Find PI to the Nth Digit
# Chudnovsky algorithm for figuring out pi

from math import factorial
from decimal import Decimal, getcontext

def calcPi_dk(limit):
    getcontext().prec=limit
    n = limit
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return str(pi)

def main():  # Wrapper function

    # Calls CalcPi with the given limit
    digits = int(input(
        "Enter the number of decimals to calculate to: "))

    pi_digits = calcPi_dk(digits)

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    i=0
    for d in pi_digits:
            print(d, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()