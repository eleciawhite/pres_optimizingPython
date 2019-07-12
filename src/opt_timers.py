#!/usr/bin/env python3
# Use timers to figure out the best way to calculate pi

import time
import w3_soln
import so_cdlane
import so_DeepakKeshari
import so_Martin_Thoma

def timer_test_1(digits):
    starttime = time.time() 
    pi_digits = w3_soln.calcPi(digits)
    endtime = time.time() 
    difftime = endtime-starttime
    print("calcPi_w3 (" + repr(digits) + ") took (s) " + repr(difftime))


def timeFunction(function, param):
    starttime = time.process_time() 
    result = function(param)
    endtime = time.process_time() 
    return endtime-starttime

def timer_test_2(digits):
    timer_test_1(digits)
    difftime = timeFunction(w3_soln.calcPi, digits)
    print("calcPi_w3 (" + repr(digits) + ") took (s) " + repr(difftime))

def timer_test_3(digits):
    difftime = timeFunction(w3_soln.calcPi, digits)
    print("calcPi_w3 (" + repr(digits) + ") took (s) " + repr(difftime))

    difftime = timeFunction(so_cdlane.calcPi, digits)
    print("so_cdlane (" + repr(digits) + ") took (s) " + repr(difftime))
 
    difftime = timeFunction(so_DeepakKeshari.calcPi, digits)
    print("so_DeepakKeshari (" + repr(digits) + ") took (s) " + repr(difftime))
 
    difftime = timeFunction(so_Martin_Thoma.calcPi, digits)
    print("so_Martin_Thoma (" + repr(digits) + ") took (s) " + repr(difftime))

def timer_test_4(digits):
    difftime = timeFunction(so_cdlane.calcPi, digits)
    print("so_cdlane (" + repr(digits) + ") took (s) " + repr(difftime))

def main():  
    # Calls CalcPi with the given limit
    digits = int(input(
        "Enter the number of decimals to calculate to: "))
    timer_test_1(digits)
    timer_test_2(digits)
    timer_test_3(digits)
    timer_test_4(digits)


if __name__ == '__main__':
    main()
