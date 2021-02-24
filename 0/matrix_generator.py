import numpy as np


def gen_matrix(n):
	eps = 1e-6
	is_det_zero = True
	matrix = None

	while is_det_zero:
		matrix = np.random.randn(n, n)
		det = np.linalg.det(matrix)
		is_det_zero = abs(det) < eps

	return matrix, det
