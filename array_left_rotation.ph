#!/bin/python3

import math
import os
import random
import re
import sys

"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .
Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description
Complete the function rotLeft in the editor below. It should return the resulting array of integers.
rotLeft has the following parameter(s):
An array of integers .
An integer , the number of rotations.

Input Format
The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform. 
The second line contains  space-separated integers .

Constraints
1 <= n <= 10^5
1 <= d <= n
1 <= a[i] <= 10^6


Output Format
Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
"""

# Complete the rotLeft function below.
def rotLeft(a, d):
    if a == 0 or d == 0:
        return a
    """
    Rotate array one position:
    arr = arr[1:-1].append(arr[0])
    repeat this step d times using for loop
    """
    l = (len(a) - d) * -1
    arr = a[l:]
    a = a[0:d]
    arr.extend(a)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
