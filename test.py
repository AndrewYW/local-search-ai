class node:
    def __init__(self, step):
        self.step = step
        self.depth = -1
        self.visited = 0


    def set_step(self, val):
        self.step = self.step + val
    
def update(test, val):
    test.step += val

def random(node):
    node.depth+= 1

if __name__ == '__main__':
    a = node(3)
    a.depth = 0
    dep = a.depth
    print(a.step)
    print(a.visited)
    print(a.depth)
    b = a
    b.visited = 1

    
    print(b.visited)
    random(b)
    print(b.depth)

    a = b

    print(a.step)
    print(a.visited)
    print(a.depth)