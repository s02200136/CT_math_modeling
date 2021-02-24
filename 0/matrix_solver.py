import time
import numpy as np
from matrix_generator import gen_matrix


def gen_and_solve(n):
	sol = None
	start = time.perf_counter()
	A, det = gen_matrix(n)
	b = np.random.randn(n)
	sol = np.zeros_like(b)
	for i in range(n):
		equation = A.copy()
		equation[:, i] = b
		sol[i] = np.linalg.det(equation) / det
	end = time.perf_counter()
	return sol, A, b, end - start
