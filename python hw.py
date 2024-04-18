# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np


def iswater(vec, i, j):
    if min(i, j) < 0 or max(i, j) >= len(vec) or j < i+2 :
        print("Index i, j error")
        return None
    else :
        m = min(vec[i], vec[j])
        ind = sum(m <= vec[(i+1):j]) == 0
        val = sum(m - vec[(i+1):j])
        return([ind, val])
    
def water(vec):
    vec = np.asarray(vec)
    ret = 0
    i = 0
    while i < len(vec)-2:
        j = len(vec)-1
        ret0 = ret
        while j >= i + 2 :
            f = iswater(vec, i, j)
            if f[0] : 
                ret += f[1]
                break
            j -= 1
        if ret > ret0 :
            i = j
        else :
            i += 1
        
    return ret
            
        
x = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(x)
print(water(x))

        
y = [6, 2, 4, 1, 5, 1, 1, 2, 3, 1]
print(y)
print(water(y))

z = [10, 2, 3, 4, 2, 5, 3, 1, 0, 0, 3, 0]
print(z)
print(water(z))




