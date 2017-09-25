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
import queue

class my_queue: 
    def __init__(self): 
        self.store = []

    def enqueue(self, value): 
        self.store.append(value)
    
    def dequeue(self): 
        value = None
        try: 
            value = self,store[0]
            if len(self.store) == 1 :
                self.store = []
            else: 
                self.store = self.store[1:]
        except: 
            pass 
        return val

    def IsEmpty(self): 
        result = False
        if len(self.store) == 0: 
            result = True
        return result

path_queue = my_queue()

def bfs(node_matrix, s, g, q):
    temp_path = [s]
    q.enqueue(temp_path)
    while q.IsEmpty() == False:
        temp_path = q.dequeue()
        last_node = temp_path[len(temp_path) - 1]
        if last_node == g: 
            print ("path : ", temp_path)
        for link_node in node_matrix[last_node]:
            if link_node not in temp_path:
                new_path = []
                new_path = temp_path + [link_node]
                q.enqueue(new_path)

def create_node_matrix(input_matrix, input_index):
    node_matrix = [[Node() for i in range(input_index)] for j in range(input_index)]
    for x in range(input_index):
        for y in range(input_index):
            node_matrix[x][y].steps = input_matrix[x][y]
    return node_matrix