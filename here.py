#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the playlist function below.
def playlist(songs):
    
    result_comb = list(combinations(songs,2))
    max_result = 0

    for item in result_comb:
        if (item[0] + item[1]) % 60 ==0:
            print("The first is : {} and the second is : {}".format(item[0],item[1]))
            max_result+=1
    
    return max_result




def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

res = playlist([10,50,90,30])
print(res)


