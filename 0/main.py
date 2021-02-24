import matplotlib.pyplot as plt
from matrix_solver import gen_and_solve

if __name__ == '__main__':
	sizes = []
	times = []
	for i in range(1, 5):
		elapsed_time = 0
		sizes.append(10 ** i)
		for _ in range(5):
			sol, A, b, time = gen_and_solve(10 ** i)
			elapsed_time += time
			print(time)
		times.append(elapsed_time / 5)
	plt.plot(sizes, times)
	plt.legend("time")
	plt.show()
