"""
Karl has an array of integers. He wants to reduce the array until all remaining elements are equal. 
Determine the minimum number of elements to delete to reach his goal.
For example, if his array is , we see that he can delete the  elements  and  leaving . He could also delete both twos and either the  or the , 
but that would take  deletions. The minimum number of deletions is .

Function Description
Complete the equalizeArray function in the editor below. It must return an integer that denotes the minimum number of deletions required.
equalizeArray has the following parameter(s):
arr: an array of integers

Input Format
The first line contains an integer , the number of elements in . 
The next line contains  space-separated integers .
Constraints
1 <= n <= 100
1 <= arr[i] <= 100

Output Format
Print a single integer that denotes the minimum number of elements Karl must delete for all elements in the array to be equal.
Sample Input
5
3 3 2 1 3
Sample Output
2 
"""
import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    """
    arr = [3,3,1,2,3,4] -> [3,3,3] return 3
    arr = [3,1,2,4] -> [3] return 3
    Algo:
    look for repeating numbers by using collections.Counter 
    sort the counts object descending
    iterate through the list looking for count > 1
    for the number with the highest highest_frequency_count
        return len(arr)- len(highest_frequency_count)
    """
    from collections import Counter
    counts = Counter(arr)
    most_common = counts.most_common(1)[0][1]
    return len(arr) - most_common

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
