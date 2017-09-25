import numpy as np
import sys
from random import randint
import tkinter as tk


def generate_random_matrix(index):
    # generates a random n-by-n matrix
    matrix = np.empty([index, index], dtype=int)
    for i in range(index):
        for j in range(index):
            if((i == index - 1) and (j == index - 1)):
                matrix[i][j] = 0
            else:
                matrix[i][j] = randint(
                    1, max(index - (i + 1), i, index - (j + 1), j))
    return matrix

def generate_visit_matrix(index):
    return np.zeros([index, index], dtype=int)

def generate_depth_matrix(index):
    m = np.empty([index, index], dtype=int)
    m.fill(-1)
    return m

def generate_str_depth_matrix(depth_matrix):
    index = len(depth_matrix[0])
    string_matrix = [['' for x in range(index)] for y in range(index)]
    for i in range(index):
        for j in range(index):
            if depth_matrix[i][j] == -1:
                string_matrix[i][j] = 'X'
            else:
                string_matrix[i][j] = str(depth_matrix[i][j])

    return string_matrix
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

def get_eval_function(depth_matrix):
    index = len(depth_matrix[0])
    if depth_matrix[index-1][index-1] == -1:
        eval = 0
        for i in range(index):
            for j in range(index):
                if depth_matrix[i][j] == -1:
                    eval -= 1
        return eval
    else:
        return depth_matrix[index-1][index-1]