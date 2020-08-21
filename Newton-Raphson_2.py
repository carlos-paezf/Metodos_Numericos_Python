# Implementacion simple del método Newton-Raphson


def nraphson(fn, x, tol = 0.0001, maxiter = 1000):
	for i in range(maxiter):
		xnew = x -fn[0](x)/fn[1](x)
		if abs(xnew - x) < tol: break
		x = xnew
	return xnew, i


y = [lambda x: 2*x**3 - 9.5*x + 7.5, lambda x: 6*x**2 - 9.5]
x, n = nraphson(y, 5)
print('The root is %f at %d iterations.' % (x,n))




#Newton-Raphson Method | Numerical Computing in Python. (2019, 17 septiembre). 
#[Vídeo]. YouTube. https://www.youtube.com/watch?v=szQUIRPrAgQ