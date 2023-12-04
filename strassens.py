import numpy as np

def strassen_multiplicaton(matrix_a, matrix_b):
    n = len(matrix_a)
    if n == 1:
        return matrix_a * matrix_b 
    a11, a12, a21, a22 = [a11[:n//2, :n//2], a12[:n//2 :n//2], a21[:n//2, :n//2], a22[:n//2, :n//2]]
    b11, b12, b21, b22 = [b11[:n//2 : n//2], b12[:n//2 :n//2], b21[:n//2, :n//2], b22[:n//2, :n//2]]
    
    p1 = strassen_multiplicaton(a11+ a22, b11 + b22)
    p2 = strassen_multiplicaton(a21+a22, b11)
    p3 = strassen_multiplicaton(a11,b12-b22)
    p4 = strassen_multiplicaton(a22, b21-b11)
    p5 = strassen_multiplicaton(a11+a12, b22)
    p6 = strassen_multiplicaton(a21-a11,b11+b21)
    p7 = strassen_multiplicaton(a12-a22, b21+b22)

    c11 = p1+p4+-p5+ p7
    c12 = p3+p5
    c21 = p2+p4
    c22= p1-p2+p3+p6

    final_matrix = np.vstack((np.hstack((c11,c12)))), np.hstack((c21,c22))
    return final_matrix
matrix_a =  [[2,4],[4,5]]
matrix_b =  [[3,6],[9,5]]
result = strassen_multiplicaton(matrix_a,matrix_b)
print(result)
