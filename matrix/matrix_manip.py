import numpy as np
import sys
from random import randint
from tkinter import *

def generate_random_matrix(index):
    #generates a random n-by-n matrix
    matrix = np.zeros([index, index], dtype=int)
    for x in np.nditer(matrix, op_flags=['readwrite']):
        x[...] = randint(1, max_steps(index))

    return matrix
def generate_gui(matrix, index):
    #creates the gui representation from a given matrix
    rows = []
    for i in range(index):
        cols = []
        for j in range(index):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, '%d' % (matrix[i][j]))
            cols.append(e)
        rows.append(cols)
def get_index_from_matrix(matrix):
    return len(matrix[0])
def generate_file_matrix(file):
    '''
    generates a matrix from a file
    file input format:
    2 2 2 4 3
    2 2 3 3 3
    3 3 2 3 3
    1 0 2 3 2
    4 3 2 4 1
    '''
    f = open(file, 'r')
    matrix = np.loadtxt(file, dtype=int, delimiter=' ')
    return matrix
def max_steps(index):
    return index
