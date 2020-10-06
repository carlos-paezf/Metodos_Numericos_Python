import numpy as np


def Newton_Raphson_Sist(F, J, x0, tol):
	x = x0
	error = 1e3
	n = 0
	while error > tol:
		dx = -np.linalg.solve(J(*x), F(*x))
		error = np.linalg.norm(dx)/np.linalg.norm(x)
		x += dx;
		n += 1
	print ("Iteraciiones: ", n)
	print ("Ans: ", x)
	return x

F = lambda x1, x2: [x1**2 - x2**2 + 2*x2, 2*x1 + x2**2 - 6]
J = lambda x1, x2: [[2*x1, -2*x2 + 2],[2, 2*x2]]
Newton_Raphson_Sist(F, J, [1,5], 1e-5)