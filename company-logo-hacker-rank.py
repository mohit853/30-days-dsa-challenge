#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


if __name__ == '__main__':
    s = input()
    comp_name_dict =defaultdict(int)
    
    for ch in s:
        comp_name_dict[ch] +=1
    
    sorted_dict = sorted(comp_name_dict.items() , key = lambda item : (-item[1],item[0]))
    
    ##[('b', 3), ('a', 2), ('c', 2), ('d', 1), ('e', 1)]
    
    count=0
    for x in sorted_dict:
        if count >=3:
            break
        print(x[0],x[1])
        count+=1
        
    
