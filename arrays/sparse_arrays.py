There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings.
For example, given input  and , we find  instances of ',  of '' and  of ''. For each query, we add an element to our return array, .
Function Description
Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each 
query string in strings.
matchingStrings has the following parameters:
strings - an array of strings to search
queries - an array of query strings

Input Format
The first line contains and integer , the size of . 
Each of the next  lines contains a string . 
The next line contains , the size of . 
Each of the next  lines contains a string .
Constraints
 
 
 .
Output Format
Return an integer array of the results of all queries in order.
Sample Input 1
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output 1
2
1
0

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    from collections import Counter
    results = []
    counts = Counter(strings)
    for query in queries:
        if query in counts:
            results.append(counts[query])
        else:
            results.append(0)
    return results
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

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

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

