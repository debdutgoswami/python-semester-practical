import numpy as np

mat1 = np.matrix(np.array([
    [1,2,3],
    [7,5,6],
    [2,9,8]
]))

mr = np.max(mat1, axis=1)

print("Row wise maximum are : ",mr)

mc = np.max(mat1, axis=0)

print("Column wise maximum are: ",mc)