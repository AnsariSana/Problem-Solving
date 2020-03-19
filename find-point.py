#!/bin/python3

import os
import sys

def findPoint(px, py, qx, qy):
    #middle point between two point can be find as mid = (start + end) // 2. so, to find endpoint end = 2*mid - start
    return 2*qx - px, 2*qy - py
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

