"""
make matrix into nodes 
intiialize your empty queue 
push start node onto the queue 
loop:
    node temp = q.pop()
        check if goal node 
            return true 
        check if visited 
        if yes: 
            continue
        if no: 
            mark as visitied 
            grab all of its neighbors 
            add them to the queue 
"""

new_matrix = np.matrix()

def matrix_to_tree_nodes(new_matrix):
    tree = {}
    for node in nodes:
        children = nodes[:]
        children.remove(node)
        tree[node] = matrix_to_tree(children)
    return tree 

def bfs():
    start_node = [0][0]
    q = 0 
    q = push(start_node)
    for1
