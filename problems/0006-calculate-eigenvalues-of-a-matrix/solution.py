def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = 1
	b = -(matrix[0][0]+matrix[1][1])
	c = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
	x1 = (- b + (b**2-4*a*c)**0.5 )/(a*2)
	x2 = (- b - (b**2-4*a*c)**0.5 )/(a*2)
	eigenvalues = [x1,x2]
	eigenvalues.sort(reverse=True)

	return eigenvalues