from .matrix_manip import *
import queue
from copy import copy, deepcopy
import math

def solve(node_matrix):
    q = queue.Queue()
    q.put(node_matrix[0][0])
    node_matrix[0][0].depth = 0
    while not q.empty():
        node = q.get()
        if node.visited == 0:
            node.visited = 1
            depth = node.depth
            for item in node.children:
                q.put(item)
                if item.depth == -1:
                    item.depth = depth + 1
def hill_climb(node_matrix, iterations):
    # Given an unsolved matrix, will attempt to solve and optimize
    # End result: stuff
    index = len(node_matrix[0])
    for step in range(iterations):
        step_matrix = create_step_matrix(node_matrix)
        temp_matrix = create_node_matrix(step_matrix)

        # Change random steps to random legal move
        temp_matrix = random_step_change(temp_matrix, index)
        #print('Node matrix: ')
        #print_step_matrix(node_matrix)
        #print('Mutated matrix: ')
        #print_step_matrix(temp_matrix)

        solve(node_matrix)
        solve(temp_matrix)
        node_eval = get_eval_from_nodes(node_matrix)
        #print('Iteration: ' + str(step))
        #print('Node eval: ' + str(node_eval))
        temp_eval = get_eval_from_nodes(temp_matrix)
        #print('Temp eval: ' + str(temp_eval))

        # If new evaluation function is better, then node matrix becomes new one
        # Node matrix's depth and visited are reset so you can run solve again
        if temp_eval >= node_eval:
            #print('Replacing node')
            node_matrix = temp_matrix
            reset_matrix(node_matrix)
        else:
            #print('Discarding changes')
            reset_matrix(node_matrix)
    #print("Final mutated matrix: ")
    #print_step_matrix(node_matrix)
    solve(node_matrix)
    return node_matrix

def random_restart(node_matrix, iterations, restarts):
    reset_matrix(node_matrix)
    index = len(node_matrix[0])
    for step in range(restarts):
        temp_matrix = deepcopy(node_matrix)
        hill_climb(temp_matrix, iterations)
        temp_eval = get_eval_from_nodes(temp_matrix)
        node_eval = get_eval_from_nodes(node_matrix)

        if temp_eval >= node_eval:
            node_matrix = temp_matrix
            reset_matrix(node_matrix)
        else:
            reset_matrix(node_matrix)
    solve(node_matrix)
def random_walk(node_matrix, iterations, prob):
    reset_matrix(node_matrix)
    index = len(node_matrix[0])

    for step in range(iterations):
        temp_matrix = node_matrix

        random_step_change(temp_matrix, index)

        roll = random.random()
        if roll > prob: #roll fail
            solve(node_matrix)
            solve(temp_matrix)
            node_eval = get_eval_from_nodes(node_matrix)
            temp_eval = get_eval_from_nodes(temp_matrix)

            if temp_eval >= node_eval:
                node_matrix = temp_matrix
                reset_matrix(node_matrix)
            else:
                reset_matrix(node_matrix)
        else:           #roll success
            node_matrix = temp_matrix
            reset_matrix(node_matrix)
    solve(node_matrix)

def annealing(node, iterations, temp, decay):

    t = temp * decay
    
    for step in range(iterations):
        clone = random_step_change(nodes)
        e_clone = get_eval_from_nodes(clone)
        e_nodes = get_eval_from_nodes(nodes)
        if e_clone > e_nodes:
            nodes = clone 
            e_nodes = e_clone
        else : 
            prob = math.exp((e_clone - e_nodes) / t)
            roll = random.random()
            if roll > prob: 
                nodes = clone 
                e_nodes = e_clone
                t = temp * decay
                reset
            else : 
                t = temp * decay
                reset

def random_step_change(nodes, index):
    #Select random matrix spot, can't change node_matrix[index-1][index-1]
    row = randint(0, index-1)
    col = randint(0, index-1)
    while row == index - 1 and col == index -1:
        row = randint(0, index-1)
        col = randint(0, index-1)
    #print('Old steps value: ' + str(nodes[row][col].steps))
    nodes[row][col].steps = randint(1, max(index-row-1, row, index-col-1, col))
    #print('Selected position: (' + str(row) + ',' + str(col) + ')')
    #print('New steps value: ' + str(nodes[row][col].steps))

    return nodes
def reset_matrix(node_matrix):
    index = len(node_matrix[0])
    for i in range(index):
        for j in range(index):
            node_matrix[i][j].visited = 0
            node_matrix[i][j].depth = -1

def print_nodes(node_matrix, index, option):
    if option == 1:
        vector = np.vectorize(lambda node: node.steps)
    if option == 2:
        vector = np.vectorize(lambda node: node.visited)
    if option == 1:
        vector = np.vectorize(lambda node: node.depth)
    print(vector(node_matrix))

if __name__=='__main__':
    matrix = [[0 for x in range(5)] for y in range(5)]
    nodes = create_node_matrix(matrix)
    random_step_change(nodes, 5)
    reset_matrix(nodes)
    print_nodes_steps(nodes, 5, 1)
