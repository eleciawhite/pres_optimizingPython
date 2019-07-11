#!/usr/bin/env python3
# Find PI to the Nth Digit
#from https://stackoverflow.com/questions/28284996/python-pi-calculation

import decimal

def calcPi(limit):
    """
    Compute Pi to the current precision.

    Examples
    --------
    >>> print(pi())
    3.141592653589793238462643383

    Notes
    -----
    Taken from https://docs.python.org/3/library/decimal.html#recipes
    """
    decimal.getcontext().prec = limit
    decimal.getcontext().prec += 2  # extra digits for intermediate steps
    three = decimal.Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return str(+s)               # unary plus applies the new precision


def main():  # Wrapper function

    # Calls CalcPi with the given limit
    digits = int(input(
        "Enter the number of decimals to calculate to: "))

    pi_digits = calcPi(digits)

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