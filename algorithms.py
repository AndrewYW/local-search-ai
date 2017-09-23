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

new_matrix = matrix
new_matrix.fill(0)

def matrix_to_tree(new_matrix):
    tree = {}
    for node in new_matrix:
        children = new_matrix[:] 
        children.remove(node)
        tree[node] = matrix_to_tree(children)
    return tree 

def start_position(tree, start):
    tree = tree[1:1]
    return tree 

def goal_state(tree, end):
    if tree[end]:
        del tree[end]
        nodes = tree.keys()
        if len(nodes) > 1:
            for node in nodes: 
                set_end(tree[node], end)
            return tree

def map_tree(tree, new_matrix, start, dist = 0):
    for node in tree:
        new_dist = dist + node_dist(new_matrix, start, node)
        if tree[node]:
            map_tree(tree[node], new_matrix, node, new_dist)
        else: 
            tree[node] = new_dist
        return tree 

def node_dist(new_matrix, start, end): 
    queue = []
    queue.append([start])
    while queue: 
        path = queue.pop(0)
        node = path[-1]
        if node == end: 
            return path
        for adj in new_matrix.get(node, []):
            new_path = list(path)
            new_path.append(adj)

    return new_matrix[start][end]