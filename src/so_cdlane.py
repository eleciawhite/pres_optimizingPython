#!/usr/bin/env python3
# Find PI to the Nth Digit
# Terms based on Gauss' refinement of Machin's formula:
# arctan(x) = x - (x^3)/3 + (x^5)/5 - (x^7)/7 + ...

from decimal import Decimal, getcontext

TERMS = [(12, 18), (8, 57), (-5, 239)]  # ala Gauss

def arctan(talj, kvot, product):

    """Compute arctangent using a series approximation"""

    summation = 0

    talj *= product

    qfactor = 1

    while talj:
        talj //= kvot
        summation += (talj // qfactor)
        qfactor += 2

    return summation

def calcPi(limit):
    getcontext().prec = limit
    product = 10 ** limit

    result = 0

    for multiplier, denominator in TERMS:
        denominator = Decimal(denominator)
        result += arctan(- denominator * multiplier, - (denominator ** 2), product)

    result *= 4  # pi == atan(1) * 4
    string = str(result/product)
    return string

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