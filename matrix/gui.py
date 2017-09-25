import tkinter as tk
from .matrix_manip import *

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

        iter_text= tk.StringVar(master, value='Enter number of iterations')
        restart_text= tk.StringVar(master, value='Enter number of restarts')
        prob_text= tk.StringVar(master, value='Enter Walk probability')
        temp_text= tk.StringVar(master, value='Enter initial temp')
        decay_text= tk.StringVar(master, value='Enter temp decay rate')
        self.iterations = tk.Entry(master,textvariable=iter_text).grid(
            row=index+1,sticky="NSEW")
        self.restarts = tk.Entry(master,textvariable=restart_text).grid(
            row=index+2,sticky="NSEW")
        self.probability = tk.Entry(master,textvariable=prob_text).grid(
            row=index+3,sticky="NSEW")
        self.temperature = tk.Entry(master,textvariable=temp_text).grid(
            row=index+1,column=1,sticky="NSEW")
        self.tempDecay = tk.Entry(master,textvariable=decay_text).grid(
            row=index+2,column=1,sticky="NSEW")

        self.solveButton = tk.Button(master,text="Solve",command=self.solution_maker).grid(
                row=index + 3,column=1,sticky="NSEW")

    def set_var(self):
        print(self.var)
    def solution_maker(self):
        if self.var == 1:
            SolveWindow(self.matrix,
                    generate_visit_matrix(self.index),
                    generate_depth_matrix(self.index), 1)
        elif self.var == 2:
            SolveWindow(self.matrix,
                    generate_visit_matrix(self.index),
                    generate_depth_matrix(self.index), 2)
        elif self.var == 3:
            SolveWindow(self.matrix,
                    generate_visit_matrix(self.index),
                    generate_depth_matrix(self.index), 3)
        elif self.var == 4:
            SolveWindow(self.matrix,
                    generate_visit_matrix(self.index),
                    generate_depth_matrix(self.index), 4)
        elif self.var == 5:
            SolveWindow(self.matrix,
                    generate_visit_matrix(self.index),
                    generate_depth_matrix(self.index), 5)
        else:
            print('No option selected')


class SolveWindow(tk.Toplevel):
    def __init__(self, step_matrix, visit_matrix, depth_matrix, option):
        tk.Toplevel.__init__(self)
        print(visit_matrix)
        print()
        print(depth_matrix)
        print('Selection option: ' + str(option))

class MakeWindow(tk.Toplevel):

    def __init__(self, message):
        tk.Toplevel.__init__(self)  # instead of super
        self.message = message
        self.display = tk.Label(self, text=message)
        self.display.pack()


# Test stuff
if __name__ == '__main__':
    root = tk.Tk()
    matrix = [[0 for x in range(5)] for y in range(5)]
    app = Application(root, matrix, 5)
    root.mainloop()
