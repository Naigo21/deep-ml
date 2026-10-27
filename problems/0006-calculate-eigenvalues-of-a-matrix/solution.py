def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	import numpy as np

	arr = np.array(matrix)
	eigenvalues, eigenvectors = np.linalg.eig(arr)
	
	ans = [float(eigenvalues[0]),float(eigenvalues[1])]
	return ans