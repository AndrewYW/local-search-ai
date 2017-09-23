import numpy as np
import sys
from random import randint
from tkinter import *


def generate_random_matrix(index):
    # generates a random n-by-n matrix
    matrix = np.zeros([index, index], dtype=int)
    '''
    for x in np.nditer(matrix, op_flags=['readwrite']):
        x[...] = randint(1, max_steps(index))
    '''
    for i in range(index):
        for j in range(index):
            if((i == index - 1) and (j == index - 1)):
                matrix[i][j] = 0
            else:
                matrix[i][j] = randint(
                    1, max(index - (i + 1), i, index - (j + 1), j))
    return matrix


def generate_gui(matrix, index):
    # creates the gui representation from a given matrix
    rows = []
    for i in range(index):
        cols = []
        for j in range(index):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, '%d' % (matrix[i][j]))
            cols.append(e)
        rows.append(cols)


def get_index_from_file(file):
    f = open(file, 'r')
    index = int(f.readline())
    f.close()
    return index


def generate_file_matrix(file):
    '''
    generates a matrix from a file
    file input format:
    n
    2 2 2 4 3
    2 2 3 3 3
    3 3 2 3 3
    1 0 2 3 2
    4 3 2 4 1
    '''
    f = open(file, 'r')
    matrix = np.loadtxt(file, dtype=int, delimiter=' ', skiprows=1)
    f.close()
    return matrix
