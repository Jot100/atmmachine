def display_matrix(matrix):
    """
    Displays the elements of a matrix.
    """
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()

def divide_matrix(matrix):
    """
    Divides a matrix into four quadrants.
    """
    rows, cols = len(matrix), len(matrix[0])
    rows //= 2
    cols //= 2
    return (
        [row[:cols] for row in matrix[:rows]],
        [row[cols:] for row in matrix[:rows]],
        [row[:cols] for row in matrix[rows:]],
        [row[cols:] for row in matrix[rows:]]
    )

def perform_strassen_multiplication(x, y):
    """
    Applies matrix multiplication using the Strassen algorithm.
    """
    if len(x) == 1:
        return [[x[0][0] * y[0][0]]]

    a, b, c, d = divide_matrix(x)
    e, f, g, h = divide_matrix(y)

    p1 = perform_strassen_multiplication(a, subtract_matrices(f, h))
    p2 = perform_strassen_multiplication(add_matrices(a, b), h)
    p3 = perform_strassen_multiplication(add_matrices(c, d), e)
    p4 = perform_strassen_multiplication(d, subtract_matrices(g, e))
    p5 = perform_strassen_multiplication(add_matrices(a, d), add_matrices(e, h))
    p6 = perform_strassen_multiplication(subtract_matrices(b, d), add_matrices(g, h))
    p7 = perform_strassen_multiplication(subtract_matrices(a, c), add_matrices(e, f))

    c11 = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = subtract_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)

    result = []
    for i in range(len(c11)):
        result.append(c11[i] + c12[i])
    for i in range(len(c21)):
        result.append(c21[i] + c22[i])

    return result

def add_matrices(x, y):
    """
    Adds two matrices element-wise.
    """
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

def subtract_matrices(x, y):
    """
    Subtracts one matrix from another element-wise.
    """
    return [[x[i][j] - y[i][j] for j in range(len(x[0]))] for i in range(len(x))]

matrix_A = [[1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [2, 2, 2, 2]]

matrix_B = [[1, 1, 1, 1],
            [2, 2, 2, 2],
            [3, 3, 3, 3],
            [2, 2, 2, 2]]

print("Matrix A:")
display_matrix(matrix_A)

print("Matrix B:")
display_matrix(matrix_B)

result_matrix = perform_strassen_multiplication(matrix_A, matrix_B)
print("Result Matrix:")
display_matrix(result_matrix)