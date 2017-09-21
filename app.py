import numpy as np
import sys
from random import randint
from tkinter import *

n = int(sys.argv[1])

def generate_array(index):
    s = (index,index)

    a = np.zeros([index,index], dtype=int)
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...]= randint(1,3)

    return a
matrix = generate_array(n)

def generate_gui(matrix):
    rows = []
    for i in range(n):
        cols = []
        for j in range(n):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, '%d' % (matrix[i][j]))
            cols.append(e)
        rows.append(cols)
'''
# def max_step(n):

#initialize variables 

    for c in n:
        c = index % n
        return c 
        
        for r in n: 
            if n == 5:
                r = {
                    '0' : n(range(0, 4)), 
                    '1' : n(range(5, 9)),
                    '2' : n(range(10, 14)),
                    '3' : n(range(15, 19)),
                    '4' : n(range(20, 24))
                } 
            return r

            elif index == 7: 
                r = {
                    '0' : n(range(0, 6)), 
                    '1' : n(range(7, 13)),
                    '2' : n(range(14, 20)),
                    '3' : n(range(21, 27)),
                    '4' : n(range(28, 34)),
                    '5' : n(range(35, 41)),
                    '6' : n(range(42, 48))
                } 
            return r 

            elif index == 9: 
                r = { 
                    '0' : n(range(0, 8)),
                    '1' : n(range(9, 17)),
                    '2' : n(range(18, 26)),
                    '3' : n(range(27, 35)),
                    '4' : n(range(36, 44)),
                    '5' : n(range(45, 53)),
                    '6' : n(range(54, 62)),
                    '7' : n(range(63, 71)),
                    '8' : n(range(72, 80))
                } 
            return r

            elif index == 9: 
                r = { 
                    '0' : n(range(0, 10)),
                    '1' : n(range(11, 21)),
                    '2' : n(range(22, 32)),
                    '3' : n(range(33, 43)),
                    '4' : n(range(44, 54)),
                    '5' : n(range(55, 65)),
                    '6' : n(range(66, 76)),
                    '7' : n(range(77, 87)),
                    '8' : n(range(88, 98)),
                    '9' : n(range(99, 109)),
                    '10' : n(range(110, 120))
                }
            return r
            
            else : 
                return 'Error'

        return #position
    return #position

'''

print(matrix)
generate_gui(matrix)


mainloop()