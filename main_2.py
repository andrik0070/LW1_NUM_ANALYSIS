from math import sqrt
import numpy as np
from pprint import pprint


def gaussSeidel(matrix, b, epsilon):
    n = len(matrix)
    x = [0.0 for i in range(n)]

    converge = False
    while not converge:
        x_new = np.copy(x)
        for i in range(n):
            first_sum = sum(matrix[i][j] * x_new[j] for j in range(i))
            second_sum = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - first_sum - second_sum) / matrix[i][i]

        # converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= epsilon
        converge = max([abs(a - b) for a, b in zip(x_new, x)]) <= epsilon

        x = x_new
    return x


pprint(gaussSeidel([[4, -3, 2], [-1, 8, 1], [1, 2, 9]], [-21, 24, -14], 0.000000000000001))
# pprint(gaussSeidel([[2, -1, 1], [1, 3, -2], [1, 2, 3]], [5, 7, 10], 0.000000000000001))

# [-8, -4,  4]
