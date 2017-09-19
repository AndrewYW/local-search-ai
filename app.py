import numpy as np
import sys
from random import randint

n = int(sys.argv[1])

def generate_array(index):
    s = (index,index)

    a = np.zeros([index,index], dtype=int)
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...]= randint(1,3)

    return a

def max_step(n):
    
print generate_array(n)
