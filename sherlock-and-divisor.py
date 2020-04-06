#!/bin/python3

import os
import sys
import math
#
# Complete the divisors function below.
#
def divisors(n):

    count = 0
    for i in range(1,int(math.sqrt(n))+1):
        
        if n % i == 0:
            n1 = i
            n2 = n // i
            # print(n1,n2)
            if n1%2 == 0:
                count += 1
            if n1 != n2:
                if n2%2 == 0:
                    count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()

