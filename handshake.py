#!/bin/python3

import os
import sys

def handshake(n):
    #n persons shake hand with every(n-1) persons but here once two person shake hand then they are not allowed to again shake hands.
    #that's why dividing by 2 to remove duplicate combinations.
    return n*(n-1)//2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = handshake(n)

        fptr.write(str(result) + '\n')

    fptr.close()
