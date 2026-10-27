def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	import numpy as np
	arr = np.array(matrix)
	means = []
	if mode=='column':
		means = arr.mean(axis = 0)
	else:
		means = arr.mean(axis =1)
	return means