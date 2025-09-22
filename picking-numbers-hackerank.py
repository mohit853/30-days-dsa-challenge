#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    
    a_dict = defaultdict(int)
    
    for x in a:
        a_dict[x] +=1
    ans=0
    
    for each_a in a:
        ans =max(ans,a_dict[each_a]+ a_dict[each_a-1],
        a_dict[each_a]+a_dict[each_a+1])
    return ans
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
