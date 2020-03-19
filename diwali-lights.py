#!/bin/python3

import os
import sys


def lights(n):
    #number of patterns of n bits can be find as 2^n. e.g 2^1 = 2, 2^2 = 4
    #here 2^n - 1 because first combination is  0 0 0 which is lights off so dont count this.
    return ((2**n) - 1) % (10**5)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
