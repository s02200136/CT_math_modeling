import time


class Timer:
	def __init__(self):
		self.start_time = 0

	def __enter__(self):
		self.start_time = time.perf_counter()
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.start_time = time.perf_counter() - self.start_time
		print(f"Time elapsed: {self.start_time} seconds")
