#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(a,d,n):
    # n = len(a)
    temp = a[:d]        #taking elements upto d bcoz in case of left rotation d elements will be append atlast and all will be shifted refer sample test cases.
    a = a[d:]
    a.extend(temp)
    
    return a
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    res = rotate(a, d, n)
    
    print(res)
