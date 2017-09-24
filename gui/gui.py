import tkinter as tk


class Application:

    def __init__(self, master, matrix, index):
        self.frame = tk.Frame(master)
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

        self.quitButton = tk.Button(
            master,
            text="QUIT",
            command=self.frame.quit).grid(
            row=index + 1,
            sticky="NSEW")

        self.solveButton = tk.Button(
            master,
            text="Solve",
            command=self.solution_maker).grid(
            row=index + 2,
            sticky="NSEW")

        self.blorbButton = tk.Button(
            master,
            text="blorb",
            fg="red",
            command=self.blorb_maker).grid(
            row=index + 3,
            sticky="NSEW")

    def solution_maker(self):
        MakeWindow('Solution')

    def blorb_maker(self):
        MakeWindow('blorb')


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
