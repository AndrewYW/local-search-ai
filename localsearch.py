import sys
from matrix.matrix_manip import *


def main():
    mode = int(input('Choose: 1) Random puzzle generation or 2) Read from file\n'))
    # Index values can only be 5, 7, 9, 11
    if(mode == 1):
        index = int(input('Enter index\n'))
        matrix = generate_random_matrix(index)
        print(matrix)
        generate_gui(matrix, index)

        mainloop()
    elif(mode == 2):
        file = input('Enter file name\n')
        print(file)
        matrix = generate_file_matrix(file)
        index = get_index_from_matrix(matrix)
        print(matrix)
        print(get_index_from_matrix(matrix))
        generate_gui(matrix, index)

        mainloop()


if __name__ == "__main__":
    main()
