import sys
from matrix.matrix_manip import *


def main():
    mode = int(input('Choose: 1) Random puzzle generation or 2) Read from file\n'))
    # Index values can only be 5, 7, 9, 11
    if(mode == 1):
        index = int(input('Enter index\n'))
        matrix = generate_random_matrix(index)
        print(matrix)
        root = tk.Tk()
        root.title('local-search-ai')
        generate_gui(matrix, index, root)

    elif(mode == 2):
        file = input('Enter file name\n')
        matrix = generate_file_matrix(file)
        index = get_index_from_file(file)
        print(matrix)
        root = tk.Tk()
        generate_gui(matrix, index, root)



if __name__ == "__main__":
    main()
