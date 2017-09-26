import tkinter as tk
from time import time
from .matrix_manip import *
from .searches import *

class Application:

    def __init__(self, master, matrix, index):
        self.frame = tk.Frame(master)
        self.matrix = matrix
        self.index = index
        self.var = tk.IntVar()
        tk.Grid.rowconfigure(master, 0, weight=1)
        tk.Grid.columnconfigure(master, 0, weight=1)

        self.frame.grid(row=0, column=0, sticky="NSEW")
        for row in range(index):
            tk.Grid.rowconfigure(master, row, weight=1)
            for col in range(index):
                tk.Grid.columnconfigure(master, col, weight=1)
                label = tk.Label(
                    self.frame, relief=tk.RIDGE, text=str(
                        matrix[row][col]))
                label.grid(row=row, column=col, sticky="NSEW")

        #var = tk.IntVar()
        self.basicSolve = tk.Radiobutton(master,text='Solve puzzle',variable=self.var,value=1,command=self.set_var).grid(
            row=1,sticky="NSEW")
        self.basicHillClimb = tk.Radiobutton(master,text='Basic Hill climbing',variable=self.var,value=2,command=self.set_var).grid(
            row=2,sticky="NSEW")
        self.randomRestart = tk.Radiobutton(master,text='HC Random Restart',variable=self.var,value=3,command=self.set_var).grid(
            row=3,sticky="NSEW")
        self.randomWalk = tk.Radiobutton(master,text='HC Random Walk',variable=self.var,value=4,command=self.set_var).grid(
            row=4,sticky="NSEW")
        self.annealing = tk.Radiobutton(master,text='Simulated Annealing',variable=self.var,value=5,command=self.set_var).grid(
            row=5,sticky="NSEW")

        self.iter_text= tk.StringVar(master, value='Enter number of iterations')
        self.restart_text= tk.StringVar(master, value='Enter number of restarts')
        self.prob_text= tk.StringVar(master, value='Enter Walk probability')
        self.temp_text= tk.StringVar(master, value='Enter initial temp')
        self.decay_text= tk.StringVar(master, value='Enter temp decay rate')
        self.iterations = tk.Entry(master,textvariable=self.iter_text).grid(
            row=index+1,sticky="NSEW")
        self.restarts = tk.Entry(master,textvariable=self.restart_text).grid(
            row=index+2,sticky="NSEW")
        self.probability = tk.Entry(master,textvariable=self.prob_text).grid(
            row=index+3,sticky="NSEW")
        self.temperature = tk.Entry(master,textvariable=self.temp_text).grid(
            row=index+1,column=1,sticky="NSEW")
        self.tempDecay = tk.Entry(master,textvariable=self.decay_text).grid(
            row=index+2,column=1,sticky="NSEW")

        self.solveButton = tk.Button(master,text="Solve",relief=tk.RAISED,command=self.solution_maker).grid(
                row=index + 3,column=1,sticky="NSEW")

    def set_var(self):
        print(self.var.get())
    def solution_maker(self):
        # The button function that solves the given matrix.
        # Generates a node matrix based on the integer matrix, then feeds into different functions
        # fields in the node matrix are adjusted by these functions, and then the result is grabbed from them.

        nodes = create_node_matrix(self.matrix)        

        if self.var.get() == 1:         #Basic solution - no additional algorithm
            #solve(nodes[0][0])
            eval_function = get_eval_from_nodes(nodes)
            solved_matrix = generate_str_depth_matrix(nodes)
            SolveWindow(solved_matrix, eval_function, '0')
        elif self.var.get() == 2:       #Basic Hill Climbing
            iterations = int(self.iter_text.get())
            print(iterations)

            start_time = time()
            #hillclimb(nodes[0][0], iterations)
            end_time = time()

            eval_function = get_eval_from_nodes(nodes)
            solved_matrix = generate_str_depth_matrix(nodes)
            elapsed = str(start_time - end_time)
            SolveWindow(solved_matrix, eval_function, elapsed)
        elif self.var.get() == 3:       #Hill CLimbing with random restart
            iterations = int(self.iter_text.get())
            restarts = int(self.restart_text.get())

            start_time = time()
            #random_restart(nodes[0][0], iterations, restarts)
            end_time = time()
            
            eval_function = get_eval_from_nodes(nodes)
            solved_matrix = generate_str_depth_matrix(nodes)
            elapsed = str(start_time - end_time)
            SolveWindow(solved_matrix, eval_function, elapsed)
        elif self.var.get() == 4:       #Hill Climbing with random walk
            iterations = int(self.iter_text.get())
            probability = float(self.prob_text.get())

            start_time = time()
            #random_walk(nodes[0][0], iterations, probability)
            end_time = time()

            eval_function = get_eval_from_nodes(nodes)
            solved_matrix = generate_str_depth_matrix(nodes)
            elapsed = str(start_time - end_time)
            SolveWindow(solved_matrix, eval_function, elapsed)
        elif self.var.get() == 5:       #Simulated Annealing
            iterations = int(self.iter_text.get())
            temp = int(self.temp_text.get())
            decay = int(self.decay_text.get())

            start_time = time()
            #annealing(nodes[0][0], interations, temp, decay)
            end_time = time()

            eval_function = get_eval_from_nodes(nodes)
            solved_matrix = generate_str_depth_matrix(nodes)
            elapsed = str(start_time - end_time)
            SolveWindow(solved_matrix, eval_function, elapsed)
        else:
            print('No option selected')

class SolveWindow(tk.Toplevel):
    def __init__(self, matrix, eval, time):
        # matrix: string matrix of depth values
        # eval: integer, evaluation function
        # time: string of a float, elapsed time of operation
        #       if time = '0', do not add time elapsed label
        tk.Toplevel.__init__(self)
        self.frame = tk.Frame(self)
        tk.Grid.rowconfigure(self.frame, 0, weight=1)
        tk.Grid.columnconfigure(self.frame, 0, weight=1)

        self.frame.grid(row=0, column=0, sticky="NSEW")
        index = len(matrix[0])
        for row in range(index):
            tk.Grid.rowconfigure(self.frame, row, weight=1)
            for col in range(index):
                tk.Grid.columnconfigure(self.frame, col, weight=1)
                label = tk.Label(
                    self, relief=tk.RIDGE, text=str(
                        matrix[row][col]))
                label.grid(row=row, column=col, sticky="NSEW")

        eval_label = tk.Label(self, text='Evaluation function:').grid(
            row=index+1, sticky="NSEW")
        eval_value = tk.Label(self, text=str(eval)).grid(
            row=index+2, sticky="NSEW")

        if time != '0':
            time_label = tk.Label(self, text='Elapsed time:').grid(
                row=index+1, column=1, sticky="NSEW")
            time_value = tk.Label(self, text=time).grid(
                row=index+2, column=1, sticky="NSEW")


# Test stuff
if __name__ == '__main__':
    root = tk.Tk()
    matrix = [['4' for x in range(5)] for y in range(5)]
    app = Application(root, matrix, 5)
    # window=SolveWindow(matrix, 11, '3.4225235')
    root.mainloop()
