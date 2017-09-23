import numpy as np
import sys
from random import randint
import tkinter as tk


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


def generate_gui(matrix, index, root):
    # creates the gui representation from a given matrix
    '''
    rows = []
    for i in range(index):
        cols = []
        for j in range(index):
            e = Entry(relief=RIDGE)
            e.grid(row=i, column=j,)
            e.insert(END, '%d' % (matrix[i][j]))
            cols.append(e)
        rows.append(cols)
    
    root = tk.Tk()
    table = tk.Frame(root)
    for row in range(index):
        for col in range(index):
            label = tk.Label(table, text=str(matrix[row][col]))
            label.grid(row=row, column=col, padx=1, pady=1)
            table[row][col]= label

    '''
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

    for row_index in range(index):
        tk.Grid.rowconfigure(root, row_index, weight=1)
        for col_index in range(index):
            tk.Grid.columnconfigure(root, col_index, weight=1)
            label = tk.Label(frame, relief=tk.RIDGE, text = str(matrix[row_index][col_index]))
            label.grid(row=row_index, column=col_index, sticky=tk.W+tk.E+tk.N+tk.S)

    root.mainloop()
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
