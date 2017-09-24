'''
import tkinter as tk

class Application():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)

        tk.Grid.rowconfigure(root, 0, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)

    def populate_matrix(self, matrix, index, frame):
        for row in range(index):
            tk.Grid.rowconfigure(root, row, weight=1)
            for col in range(index):
                tk.Grid.columnconfigure(root, col, weight=1)
                label = tk.Label(frame, relief=tk.RIDGE, text = str(matrix[row][col]))

    def generate_buttons(self):
        btn = tk.Button(root, text="QUIT", fg="red",
                              command=root.destroy)
        tk.Grid.rowconfigure(root, index+1, weight=1)
        btn.grid(row=index+1, sticky=tk.W+tk.E+tk.N+tk.S)
        btn = tk.Button(root, text="Solve", fg="red",
                                command=self.solve_matrix)
        tk.Grid.rowconfigure(root, index+2, weight=1)
        btn.grid(row=index+2, sticky=tk.W+tk.E+tk.N+tk.S)
        btn = tk.Button(root, text="Populate", fg="red",
                                command=self.populate_matrix)
        tk.Grid.rowconfigure(root, index+3, weight=1)
        btn.grid(row=index+3, sticky=tk.W+tk.E+tk.N+tk.S)
    def solve_matrix(matrix):
        print('blorp')

root = tk.Tk()
app = Application(root)
matrix = [[0 for x in range(3)] for y in range(3)]
app.populate_matrix(matrix, 3, root.frame)
root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

    root = tk.Tk()
    Application(root).grid(row=0, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
    root.populate_matrix(matrix, index)
    root.generate_buttons()
    root.mainloop()


'''
import tkinter as tk


class Application:
    def __init__(self, master, matrix, index):
        self.frame = tk.Frame(master)
        tk.Grid.rowconfigure(root, 0, weight=1)
        tk.Grid.columnconfigure(root, 0, weight=1)

        self.frame.grid(row=0, column=0, sticky="NSEW")
        for row in range(index):
            tk.Grid.rowconfigure(root, row, weight=1)
            for col in range(index):
                tk.Grid.columnconfigure(root, col, weight=1)
                label = tk.Label(self.frame, relief=tk.RIDGE, text = str(matrix[row][col]))
                label.grid(row=row, column=col, sticky="NSEW")


        #tk.Grid.rowconfigure(root, index+1, weight=1)
        self.quitButton = tk.Button(root, text="QUIT",
                            command=self.frame.quit).grid(row=index+1,sticky="NSEW")

        #tk.Grid.rowconfigure(root, index+2, weight=1)
        self.solveButton = tk.Button(root, text="Solve",
                            command=self.solution_maker).grid(row=index+2, sticky="NSEW")

        self.blorbButton = tk.Button(root, text="blorb", fg="red",
                                command=self.blorb_maker).grid(row=index+3, sticky="NSEW")
        #tk.Grid.rowconfigure(root, index+3, weight=1)


    def solution_maker(self):
        MakeWindow('Solution')
    def blorb_maker(self):
        MakeWindow('blorb')


class MakeWindow(tk.Toplevel):
    def __init__(self, message):
        tk.Toplevel.__init__(self) #instead of super
        self.message = message
        self.display = tk.Label(self, text=message)
        self.display.pack()


#Test stuff
if __name__ == '__main__':
    root = tk.Tk()
    matrix = [[0 for x in range(5)] for y in range(5)]
    app = Application(root, matrix, 5)
    root.mainloop()