def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	import numpy as np
	arr = np.array(matrix)
	
	return arr * scalar