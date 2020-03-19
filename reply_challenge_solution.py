#-------------------------------------------Problem Definition----------------------------------------------- 


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n,queries):    
    array=[]
    for index in range(n):
        array.append(0)
    for query in queries:
       
        array[query[0]-1] += query[2]
        if query[1] < n:
            array[query[1]] -= query[2]
            
       


        

    temp,max = array[0],array[0]
    for i in range(1,len(array)):

        temp += array[i]
        if temp > max:
            max = temp
        
    return max

if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    # fptr.write(str(result) + '\n')
    # fptr.close()
