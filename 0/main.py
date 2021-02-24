import numpy as np
import matplotlib.pyplot as plt
from matrix_solver import gen_and_solve

if __name__ == '__main__':
	sizes = []
	times = []
	for i in range(1, 4):
		sol, A, b, time = gen_and_solve(10**i)
		sizes.append(10**i)
		times.append(time)
		print(time)
	plt.plot(sizes, times)
	plt.legend("time")
	plt.show()
