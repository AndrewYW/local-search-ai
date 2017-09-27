from .matrix_manip import *
from random import random
import queue
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
    # Return value: post-solve node matrix
    reset_matrix(node_matrix)
    index = len(node_matrix[0])
    for step in range(iterations):
        step_matrix = create_step_matrix(node_matrix)
        temp_matrix = create_node_matrix(step_matrix)

        temp_matrix = random_step_change(temp_matrix, index)

        solve(node_matrix)
        solve(temp_matrix)
        node_eval = get_eval_from_nodes(node_matrix)
        temp_eval = get_eval_from_nodes(temp_matrix)

        # If new evaluation function is better, then node matrix becomes new one
        # Node matrix's depth and visited are reset so you can run solve again
        if temp_eval >= node_eval:
            node_matrix = temp_matrix
            reset_matrix(node_matrix)
        else:
            reset_matrix(node_matrix)
    solve(node_matrix)
    return node_matrix

def random_restart(node_matrix, iterations, restarts):
    reset_matrix(node_matrix)
    index = len(node_matrix[0])
    for step in range(restarts):
        temp_matrix = hill_climb(node_matrix, iterations)
        temp_eval = get_eval_from_nodes(temp_matrix)
        node_eval = get_eval_from_nodes(node_matrix)

        if temp_eval >= node_eval:
            node_matrix = temp_matrix
            reset_matrix(node_matrix)
            print('Hill climb accepted on step: ' + str(step))
        else:
            reset_matrix(node_matrix)
    solve(node_matrix)
    return node_matrix
def random_walk(node_matrix, iterations, prob):
    reset_matrix(node_matrix)
    index = len(node_matrix[0])

    for step in range(iterations):
        step_matrix = create_step_matrix(node_matrix)
        temp_matrix = create_node_matrix(step_matrix)

        temp_matrix = random_step_change(temp_matrix, index)

        roll = random()
        print('Roll: ' + str(roll))
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
    return node_matrix

def annealing(nodes, iterations, temp, decay):

    t = temp
    index = len(nodes[0])
    
    for step in range(iterations):
        step_matrix = create_step_matrix(nodes)
        temp_matrix = create_node_matrix(step_matrix)

        temp_matrix = random_step_change(temp_matrix, index)
        print_depth_matrix(temp_matrix)
        solve(temp_matrix)
        print('temp matrix: ')
        print_step_matrix(temp_matrix)
        solve(nodes)
        print('original matrix: ')
        print_step_matrix(nodes)
        print('Temp matrix post solve(nodes)')
        print_step_matrix(temp_matrix)
        print('temp depth matrix')
        print_depth_matrix(temp_matrix)
        e_clone = get_eval_from_nodes(temp_matrix)
        e_nodes = get_eval_from_nodes(nodes)
        print('e_clone and e_node')
        print(str(e_clone) + ' ' + str(e_nodes))
        if e_clone > e_nodes:
            print('Temp eval higher than original, accept at step: ' + str(step))
            nodes = temp_matrix
            e_nodes = e_clone
        else : 
            prob = math.exp((e_clone - e_nodes) / t)
            roll = random()
            print('Probability: ' + str(prob))
            print('Roll: ' + str(roll))
            if roll > prob:     
                print('Roll succeed at step: ' + str(step))
                nodes = temp_matrix
                t *= decay
                reset_matrix(nodes)
            else : 
                print('Roll failed at step: ' + str(step))
                t *= decay
                reset_matrix(nodes)
    solve(nodes)
    return nodes
def random_step_change(nodes, index):
    #Select random matrix spot, can't change node_matrix[index-1][index-1]
    row = randint(0, index-1)
    col = randint(0, index-1)
    while row == index - 1 and col == index -1:
        row = randint(0, index-1)
        col = randint(0, index-1)
    print('Old steps value: ' + str(nodes[row][col].steps))
    nodes[row][col].steps = randint(1, max(index-row-1, row, index-col-1, col))

    #Must regenerate children for changed index:
    nodes[row][col].children[:]=[]
    nodes[row][col].get_up(nodes)
    nodes[row][col].get_down(nodes)
    nodes[row][col].get_left(nodes)
    nodes[row][col].get_right(nodes)
    print('Selected position: (' + str(row) + ',' + str(col) + ')')
    print('New steps value: ' + str(nodes[row][col].steps))

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
