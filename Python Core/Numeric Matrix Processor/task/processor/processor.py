from utilities import *
choice = -1
while choice != 0:
    result = False
    choice = int(input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: """))

    if choice == 1:
        matrices = get_matrices(2)
        result = matrix_sum(*matrices)
        if not result:
            print('The operation cannot be performed.\n')
        else:
            print(f'The result is:\n{matrix_to_str(result)}')

    if choice == 2:
        matrix = get_matrices(1)[0]
        constant = float(input('Enter constant: '))
        result = scalar_multiplication(matrix, constant)
        if not result:
            print('The operation cannot be performed.\n')
        else:
            print(f'The result is:\n{matrix_to_str(result)}')

    if choice == 3:
        matrices = get_matrices(2)
        result = matrix_multiplication(*matrices)
        if not result:
            print('The operation cannot be performed.\n')
        else:
            print(f'The result is:\n{matrix_to_str(result)}')

    if choice == 4:
        transpose = int(input("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: """))

        if transpose == 1:
            matrix = get_matrices(1)[0]
            result = transpose_main(matrix)
            if not result:
                print('The operation cannot be performed.\n')
            else:
                print(f'The result is:\n{matrix_to_str(result)}')

        if transpose == 2:
            matrix = get_matrices(1)[0]
            result = transpose_side(matrix)
            if not result:
                print('The operation cannot be performed.\n')
            else:
                print(f'The result is:\n{matrix_to_str(result)}')

        if transpose == 3:
            matrix = get_matrices(1)[0]
            result = transpose_vertical(matrix)
            if not result:
                print('The operation cannot be performed.\n')
            else:
                print(f'The result is:\n{matrix_to_str(result)}')

        if transpose == 4:
            matrix = get_matrices(1)[0]
            result = transpose_horizontal(matrix)
            if not result:
                print('The operation cannot be performed.\n')
            else:
                print(f'The result is:\n{matrix_to_str(result)}')

    if choice == 5:
        matrix = get_matrices(1)[0]
        result = determinant(matrix)
        if not result:
            print('The operation cannot be performed.\n')
        else:
            print(f'The result is:\n{result}\n')

    if choice == 6:
        matrix = get_matrices(1)[0]
        result = inverse(matrix)
        if not result:
            print("This matrix doesn't have an inverse.\n")
        else:
            print(f'The result is:\n{matrix_to_str(result)}')