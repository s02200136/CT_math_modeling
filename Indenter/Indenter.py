class Indenter:
	def __init__(self):
		self.indent_count = 0

	def __enter__(self):
		self.indent_count += 1
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.indent_count -= 1

	def print(self, s):
		for _ in range(self.indent_count):
			print("\t", end='')
		print(s)


if __name__ == '__main__':
	with Indenter() as indent:
		indent.print('hi')
		with indent:
			indent.print("hello")
			with indent:
				indent.print('bonjour')
		indent.print('hey')
