#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    # Create a copy of the input matrix
    new_matrix = matrix.copy()

    # Iterate over the rows of the matrix
    for a in range(len(matrix)):

        # Square each element in the row using a lambda function and map
        new_matrix[a] = list(map(lambda x: x**2, matrix[a]))

    return new_matrix
