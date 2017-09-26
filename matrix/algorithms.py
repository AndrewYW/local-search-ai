import Queue
from .matrix_manip import *

q = Queue.Queue() #FIFO: use get to push into back of queue and get to pull from front of queue 

def bfs(nodes): 
    q.put(nodes[0][0])
    nodes[0][0].depth = 0 
    while not q.empty(): 
        node = q.get()
        node.visited = 1 
        depth = node.depth
        if node.children: 
            for x in range(len(node.children)):
                if node.children[x].visited == 0:
                    q.put(node.children[x])
                    node.children[x].depth = depth + 1 
                    
                        




    




