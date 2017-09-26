import numpy as np
import sys
from random import randint
import tkinter as tk
sys.setrecursionlimit(50000)
class Node:
    #The node class acts as a structure holding each matrix position's children, matrix location (x,y), and whether or not it has been visited, and the depth.
    #Initialization updates the values accordingly and appends nodes to a list, .children.
    #The get-depth() function is used for printing out the solution string matrix, which displays either the steps needed to visit a node or an 'X' if it can't be reached.
    def __init__(self, matrix, x_pos, y_pos):
        self.steps = int(matrix[x_pos][y_pos])
        self.visited = 0
        self.depth = -1
        self.children = []
        self.matrix = matrix
        self.x = x_pos
        self.y = y_pos
        #self.get_children(matrix)
        self.index = len(matrix[0])
        
    def get_pos(self):
        return str('(' + str(self.x) + ',' + str(self.y) + ')')   
    def get_depth(self):
        if self.depth == -1:
            return 'X'
        else:
            return str(self.depth)
    def get_up(self, nodes):
        up = self.x - self.steps
        if up >= 0:
            #print('Position: [' + str(self.x) + '][' + str(self.y) + ']')
            print('adding up at position[' + str(up) + '][' + str(self.y) + ']')
            self.children.append(get_node(nodes, up, self.y))
    def get_down(self, nodes):
        down = self.x + self.steps
        if down < self.index:
            #print('Position: [' + str(self.x) + '][' + str(self.y) + ']')
            print('adding down at position[' + str(down) + '][' + str(self.y) + ']')
            self.children.append(get_node(nodes, down, self.y))
    def get_left(self, nodes):
        left = self.y - self.steps
        if left >= 0:
            #rint('Position: [' + str(self.x) + '][' + str(self.y) + ']')
            print('adding left at position[' + str(self.x) + '][' + str(left) + ']')
            self.children.append(get_node(nodes, self.x, left))
    def get_right(self, nodes):
        right = self.y + self.steps
        if right < self.index:
            #print('Position: [' + str(self.x) + '][' + str(self.y) + ']')
            print('adding right at position[' + str(self.x) + '][' + str(right) + ']')
            self.children.append(get_node(nodes, self.x, right))
    def get_children(self, matrix):
        index = len(matrix[0])
        #up direction
        up = self.x - self.steps
        if up >= 0:
            self.children.append(Node(matrix, up, self.y))
        
        #down
        down = self.x + self.steps
        if down < index:
            self.children.append(Node(matrix, down, self.y))

        #left
        left = self.y - self.steps
        if left >= 0:
            self.children.append(Node(matrix, self.x, left))

        #right 
        right = self.y + self.steps
        if right < index:
            self.children.append(Node(matrix, self.x, right))
def get_node(nodes, x, y):
    return nodes[x][y]
def create_node_matrix(matrix):
    #creates a matrix of nodes given an integer matrix formed either randomly or from a file.
    index = len(matrix[0])
    #node_matrix = [[Node(matrix, i, j) for i in range(index)] for j in range(index)]
    node_matrix = []
    for i in range(index):
        node_matrix.append([])
        for j in range(index):
            node_matrix[i].append(Node(matrix, i, j))
    for row, i in enumerate(node_matrix):
        for col, j in enumerate(i):
            if row == index and col == index:
                pass
            else:
                print('position [' + str(row) + '][' + str(col) + ']')
                print('Step value: ' + str(node_matrix[row][col].steps))
                node_matrix[row][col].get_up(node_matrix)
                node_matrix[row][col].get_down(node_matrix)
                node_matrix[row][col].get_left(node_matrix)
                node_matrix[row][col].get_right(node_matrix)
    print('nodes[4][3]')
    drn = len(node_matrix[4][3].children)
    drp = len(node_matrix[2][1].children)
    for x in range(drn):
        print(node_matrix[4][3].children[x].get_pos())
        print(node_matrix[4][3].children[x].steps)
    print('nodes[2][1]')
    for x in range(drp):
        print(node_matrix[2][1].children[x].get_pos())
        print(node_matrix[2][1].children[x].steps)
    return node_matrix

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

def generate_str_depth_matrix(node_matrix):
    index = len(node_matrix[0])
    string_matrix = [['' for x in range(index)] for y in range(index)]
    for i in range(index):
        for j in range(index):
            if node_matrix[i][j].depth == -1:
                string_matrix[i][j] = 'X'
            else:
                string_matrix[i][j] = str(node_matrix[i][j].depth)

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

#deprecated
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

def get_eval_from_nodes(node_matrix):
    index = len(node_matrix[0])
    if node_matrix[index-1][index-1].depth == -1:
        eval = 0
        for i in range(index):
            for j in range(index):
                if node_matrix[i][j].depth == -1:
                    eval -= 1
        return eval
    else:
        return node_matrix[index-1][index-1].depth