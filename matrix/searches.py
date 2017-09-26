from .matrix_manip import *
import queue

def solve(node_matrix):
    q = queue.Queue()
    q.put(node_matrix[0][0])
    node_matrix[0][0].depth = 0
    #print('')
    while not q.empty():
        node = q.get()
        if node.visited == 0:
            print('Checking node at: ' + node.get_pos())
            print('Depth value: ' + str(node.depth))
            node.visited = 1
            depth = node.depth
            for item in node.children:
                q.put(item)
                if item.depth == -1:
                    item.depth = depth + 1
            print('Placed ' + str(len(node.children)) + ' children into queue')
    print('end queue')
    '''
    while not q.empty(): 
        node = q.get()
        node.visited = 1 
        if node.visited == 0:
            depth = node.depth
        if node.children: 
            #print(node.children)
            for x in range(len(node.children)):
                #print(node.children[x].children)
                if node.children[x].visited == 0:
                    
                    print('unvisited, adding node')
                    print('PARENT NODE: ' + node.get_pos())
                    print('Position: ' + node.children[x].get_pos())
                    print('step value: ' + str(node.children[x].steps))
                    print('set depth: ' + str(depth+1))
                    
                    q.put(node.children[x])
                    node.children[x].depth = depth + 1 
                    node.children[x].visited = 1
                    #print(len(node.children[x].children))
    # print('queue empty')
    '''
def hill_climb(node_matrix, iterations):
    # Given an unsolved matrix, will attempt to solve and optimize
    # End result: stuff
    index = len(node_matrix[0])
    for step in range(iterations):
        temp_matrix = node_matrix

        # Change random steps to random legal move
        random_step_change(temp_matrix, index)

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

def random_restart(node_matrix, iterations, restarts):
    reset_matrix(node_matrix)
    index = len(node_matrix[0])
    for step in range(restarts):
        temp_matrix = node_matrix
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
    return 0
def random_step_change(node_matrix, index):
    #Select random matrix spot, can't change node_matrix[index-1][index-1]
    i = randint(1, index-1)
    j = randint(1, index-1)
    while i == index-1 and j == index-1:
        i = randint(1, index-1)
        j = randint(1, index-1)

    #Generate new step value
    node_matrix[i][j].steps = randint(
        1, max(index - (i + 1), i, index - (j + 1), j))
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
