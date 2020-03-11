#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seq = [[] for i in range(n)]
    last_answers = []
    last_answer = 0
    for query in queries:
        query_type, x, y = query
        if query_type == 1:
            seq_index = (x ^ last_answer) % n
            seq[seq_index].append(y)
            #print(seq)
        elif query_type == 2:
            seq_index = (x ^ last_answer) % n
            index = y % len(seq[seq_index])
            last_answer = seq[seq_index][index]
            last_answers.append(last_answer)
        else:
            print("incorrect query type. must be 1 or 2")

    return last_answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
