#!/bin/python3

import os
import sys

def summingSeries(n):
    #In given problem Tn equation when expands will be Tn = 2*n - 1 (2n - 1) is odd number.
    #So for each Tn term number is odd and Sn is summation of Tn i.e sum of odd numbers. Sum of odd numbers can be find as n^2 
    #e.g sum of 3 odd numbers will be 9 i.e 1+3+5
    return ((n)**2)  % ((10**9) + 7) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()
