#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):
    # Split on spaces (preserving multiple spaces), capitalize first char of each word
    return " ".join(word.capitalize() for word in s.split(" "))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
    
    

'''Sample Input
chris alan

 Sample Output
Chris Alan'''