from math import sqrt
import numpy as np
from pprint import  pprint


def gaussSeidel(matrix, b, epsilon):
    n = len(matrix)
    x = [.7 for i in range(n)]

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            first_sum = sum(matrix[i][j] * x_new[j] for j in range(i))
            second_sum = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - first_sum - second_sum) / matrix[i][i]

        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= epsilon
        x = x_new

    return x


pprint(gaussSeidel([[4, -3, 2], [1, 2, 9], [-1, 8, 1]], [-21, -14, 24], 50))
