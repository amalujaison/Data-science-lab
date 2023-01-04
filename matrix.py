import numpy as np
A = np.array([[5, 8, 7], [9, 14, 12], [13, 2, 6]])
B = np.array([[3, 7, 4], [10, 5, 6], [7, 9, 8]])
C = np.array([[4, 1, 3], [2, 3, 9], [7, 6, 5]])
print(np.multiply(A,B))
print(4*np.square(B))
print(np.divide(C,4))
print((np.multiply(A, B))+(4*np.square(B))-(np.divide(C, 4)))
