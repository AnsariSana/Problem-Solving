#!/bin/python3

import math
import os
import random
import re
import sys

def matchingStrings(strings, queries):
    strings_count = dict()
    query_count = []
    for string in strings:
        try:
            strings_count[string] += 1
        except:
            strings_count[string] = 1

    for query in queries:
        try:
            query_count.append(strings_count[query])
        except:
            query_count.append(0)

    return query_count
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)
    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
