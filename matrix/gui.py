import tkinter as tk
from time import time
from .searches import *
from .writer import *

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
        self.genetics = tk.Radiobutton(master, text='Genetic Alg',variable=self.var,value=6,command=self.set_var).grid(
            row=1, column = 1,sticky="NSEW")

        self.iter_text= tk.StringVar(master, value='Iterations')
        self.restart_text= tk.StringVar(master, value='Restarts/Pop_size')
        self.prob_text= tk.StringVar(master, value='Walk/Crossover')
        self.temp_text= tk.StringVar(master, value='Temp/Elitism')
        self.decay_text= tk.StringVar(master, value='Decay/Pickrate')
        self.mutate= tk.StringVar(master, value='Mutation')
        self.iterations = tk.Entry(master,textvariable=self.iter_text).grid(
            row=index+1,sticky="NSEW")
        self.restarts = tk.Entry(master,textvariable=self.restart_text).grid(
            row=index+2,sticky="NSEW")
        self.probability = tk.Entry(master,textvariable=self.prob_text).grid(
            row=index+3,sticky="NSEW")
        self.mutation = tk.Entry(master,textvariable=self.mutate).grid(
            row=index+4,sticky="NSEW")
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
            solve(nodes)
            eval_function = get_eval_from_nodes(nodes)
            solved_matrix = generate_str_depth_matrix(nodes)
            SolveWindow(solved_matrix, eval_function, '0')
            nodes = create_node_matrix(self.matrix)
        elif self.var.get() == 2:       #Basic Hill Climbing
            iterations = int(self.iter_text.get())

            start_ms = int(round(time() * 1000))
            solution = hill_climb(nodes, iterations)
            end_ms = int(round(time() * 1000)) - start_ms

            eval_function = get_eval_from_nodes(solution)
            solved_matrix = generate_str_depth_matrix(solution)
            elapsed = str(end_ms)
            SolveWindow(solved_matrix, eval_function, elapsed)
            write_hill(len(nodes), eval_function, iterations, elapsed)
            nodes = create_node_matrix(self.matrix)
        elif self.var.get() == 3:       #Hill CLimbing with random restart
            iterations = int(self.iter_text.get())
            restarts = int(self.restart_text.get())

            start_ms = int(round(time() * 1000))
            sol = random_restart(nodes, iterations, restarts)
            end_ms = int(round(time() * 1000)) - start_ms
            
            eval_function = get_eval_from_nodes(sol)
            solved_matrix = generate_str_depth_matrix(sol)
            elapsed = str(end_ms)
            SolveWindow(solved_matrix, eval_function, elapsed)
            write_restart(len(nodes),restarts,eval_function,iterations, elapsed)
            nodes = create_node_matrix(self.matrix)
        elif self.var.get() == 4:       #Hill Climbing with random walk
            iterations = int(self.iter_text.get())
            probability = float(self.prob_text.get())

            start_ms = int(round(time() * 1000))
            sol = random_walk(nodes, iterations, probability)
            end_ms = int(round(time() * 1000)) - start_ms

            eval_function = get_eval_from_nodes(sol)
            solved_matrix = generate_str_depth_matrix(sol)
            elapsed = str(end_ms)
            SolveWindow(solved_matrix, eval_function, elapsed)
            write_walk(len(nodes), eval_function, iterations, probability, elapsed)
            nodes = create_node_matrix(self.matrix)
        elif self.var.get() == 5:       #Simulated Annealing
            iterations = int(self.iter_text.get())
            temp = int(self.temp_text.get())
            decay = float(self.decay_text.get())

            start_ms = int(round(time() * 1000))
            sol = annealing(nodes, iterations, temp, decay)
            end_ms = int(round(time() * 1000)) - start_ms

            eval_function = get_eval_from_nodes(sol)
            solved_matrix = generate_str_depth_matrix(sol)
            elapsed = str(end_ms)
            SolveWindow(solved_matrix, eval_function, elapsed)
            write_anneal(len(nodes), eval_function, iterations, temp, decay, elapsed)
            nodes = create_node_matrix(self.matrix)
        elif self.var.get() == 6:       #Genetics
            pop_size = int(self.restart_text.get())
            iterations = int(self.iter_text.get())
            elite_rate = float(self.temp_text.get())
            tourney_rate = float(self.decay_text.get())
            crossover = float(self.prob_text.get())
            mutate = float(self.mutate.get())

            start_ms = int(round(time() * 1000))
            sol = genetics(self.matrix, pop_size, iterations, elite_rate, tourney_rate, crossover, mutate)
            end_ms = int(round(time() * 1000)) - start_ms
            solve(sol)
            eval_function = get_eval_from_nodes(sol)
            solved_matrix = generate_str_depth_matrix(sol)
            elapsed = str(end_ms)
            SolveWindow(solved_matrix, eval_function, elapsed)
            write_genes(len(nodes), eval_function, iterations, elapsed, elite_rate, tourney_rate, crossover)
            nodes = create_node_matrix(self.matrix)

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
            row=1, column=index+1, sticky="NSEW")
        eval_value = tk.Label(self, text=str(eval)).grid(
            row=2, column=index+2, sticky="NSEW")

        if time != '0':
            time += ' ms'
            time_label = tk.Label(self, text='Elapsed time:').grid(
                row=3, column=index+1, sticky="NSEW")
            time_value = tk.Label(self, text=time).grid(
                row=4, column=index+2, sticky="NSEW")


# Test stuff
if __name__ == '__main__':
    root = tk.Tk()
    matrix = [['4' for x in range(5)] for y in range(5)]
    app = Application(root, matrix, 5)
    # window=SolveWindow(matrix, 11, '3.4225235')
    root.mainloop()
