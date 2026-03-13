import numpy as np

matrix = np.random.randint(1,100,size=(5,5))
print(matrix)
matrix_mean = np.mean(matrix)
matrix_median = np.median(matrix)
matrix_std = np.std(matrix)

print(f"Mean: {matrix_mean}")
print(f"Median: {matrix_median}")
print(f"Standard Deviation: {matrix_std}")