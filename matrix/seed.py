from .matrix_manip import *
from .searches import solve

class Seed:
    def __init__(self, matrix):
        self.matrix = matrix
        self.index = len(matrix)
        self.set_eval()
    def set_eval(self):
        temp = create_node_matrix(self.matrix)
        solve(temp)
        self.eval = get_eval_from_nodes(temp)
        del temp
    def set_nodes(self):
        self.nodes = create_node_matrix(matrix)
