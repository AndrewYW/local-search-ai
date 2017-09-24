import numpy as np

class Node:
    def __init__(self):
        self.steps = 0
        self.visited = 0
        self.depth = -1

    def get_depth(self):
        if self.depth == -1:
            return 'X'
        else:
            return str(self.depth)


def create_node_matrix(input_matrix, input_index):
    node_matrix = [[Node() for i in range(input_index)] for j in range(input_index)]
    for x in range(input_index):
        for y in range(input_index):
            node_matrix[x][y].steps = input_matrix[x][y]

    return node_matrix

def get_eval_function(node_matrix, index):


#testing
if __name__ == '__main__':
    matrix = [[3 for x in range(5)] for y in range(5)]
    nodes = create_node_matrix(matrix, 5)
    
    for x in range(5):
        for y in range(5):
            print(nodes[x][y].steps, end="")
        print()

    for x in range(5):
        for y in range(5):
            print(nodes[x][y].depth, end="")
        print()
