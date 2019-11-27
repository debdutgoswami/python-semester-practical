import numpy as np

mat1 = np.matrix(np.array([
    [1,2,3],
    [4,5,6],
    [7,2,9]
]))

mat2 = np.matrix(np.array([
    [7,6,5],
    [3,8,4],
    [1,2,1]
]))

mat3 = np.matmul(mat1,mat2)

print(mat3)