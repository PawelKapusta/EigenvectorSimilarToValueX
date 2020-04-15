import numpy as np
import scipy.sparse.linalg as linalg
a = np.matrix([[2.0, -1.0, 0.0, 0.0, 1.0],
               [-1.0, 2.0, 1.0, 0.0, 0.0],
               [0.0, 1.0, 1.0, 1.0, 0.0],
               [0.0, 0.0, 1.0, 2.0, -1.0],
               [1.0, 0.0, 0.0, -1.0 ,2.0]])
eigenValues, eigenVectors = linalg.eigs(a, k=1, sigma=0.38197)
print("Eigenvector of matrix A: ")
print (eigenValues.real)
print("Eigenvector for 0.38197 is: ")
print (eigenVectors.real)