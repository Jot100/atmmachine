
def strassen_multiplication(matrix_a, matrix_b):
    n = len(matrix_a)
    if n == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]

    # Split matrices into quadrants
    a11, a12 = [row[:n//2] for row in matrix_a[:n//2]], [row[n//2:] for row in matrix_a[:n//2]]
    a21, a22 = [row[:n//2] for row in matrix_a[n//2:]], [row[n//2:] for row in matrix_a[n//2:]]

    b11, b12 = [row[:n//2] for row in matrix_b[:n//2]], [row[n//2:] for row in matrix_b[:n//2]]
    b21, b22 = [row[:n//2] for row in matrix_b[n//2:]], [row[n//2:] for row in matrix_b[n//2:]]

    # Recursive calls
    p1 = strassen_multiplication([[a11[i][j] + a22[i][j] for j in range(n//2)] for i in range(n//2)],
                 [[b11[i][j] + b22[i][j] for j in range(n//2)] for i in range(n//2)])
    p2 = strassen_multiplication([[a21[i][j] + a22[i][j] for j in range(n//2)] for i in range(n//2)], b11)
    p3 = strassen_multiplication(a11, [[b12[i][j] - b22[i][j] for j in range(n//2)] for i in range(n//2)])
    p4 = strassen_multiplication(a22, [[b21[i][j] - b11[i][j] for j in range(n//2)] for i in range(n//2)])
    p5 = strassen_multiplication([[a11[i][j] + a12[i][j] for j in range(n//2)] for i in range(n//2)], b22)
    p6 = strassen_multiplication([[a21[i][j] - a11[i][j] for j in range(n//2)] for i in range(n//2)],
                                  [[b11[i][j] + b21[i][j] for j in range(n//2)] for i in range(n//2)])
    p7 = strassen_multiplication([[a12[i][j] - a22[i][j] for j in range(n//2)] for i in range(n//2)],
                                  [[b21[i][j] + b22[i][j] for j in range(n//2)] for i in range(n//2)])

    # Compute the resulting quadrants
    c11 = [[p1[i][j] + p4[i][j] - p5[i][j] + p7[i][j] for j in range(n//2)] for i in range(n//2)]
    c12 = [[p3[i][j] + p5[i][j] for j in range(n//2)] for i in range(n//2)]
    c21 = [[p2[i][j] + p4[i][j] for j in range(n//2)] for i in range(n//2)]
    c22 = [[p1[i][j] - p2[i][j] + p3[i][j] + p6[i][j] for j in range(n//2)] for i in range(n//2)]

    # Combine the resulting quadrants into the final matrix
    top = (c11, c12)
    bottom = (c21, c22)
    final_matrix = (top, bottom)

    return final_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix_a = [[2, 4], 
            [4, 5]]
print("Matrix A:")
print_matrix(matrix_a)

matrix_b = [[3, 6], 
            [9, 5]]
print("\nMatrix B:")
print_matrix(matrix_b)

result = strassen_multiplication(matrix_a, matrix_b)

print("\nResult Matrix:")
print_matrix(result)
'''O(n^log2(7)) = O(n^2.81) is the time complexity.
Description: The matrix multiplication algorithm is based on Strassen's algorithm. Compared to the naïve matrix multiplication algorithm, it is more efficient. Compared to the O(n^3) time complexity of the naïve matrix multiplication technique, the time complexity of Strassen's approach is around O(n^log2(7)). By lowering the necessary number of multiplications, it makes this improvement.'''