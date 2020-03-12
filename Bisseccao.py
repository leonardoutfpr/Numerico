import numpy as np
import math

def calculo(X):
	f = -4 + 8*X - (5*X**2) + (X**3) 
	return (f)


def bisseccao(x1, x2, imax, ea):
	iter = 0
	
	print(calculo(2))
	
	while (iter <= imax and abs(calculo(x1)*calculo(x2)) > ea):
		iter = iter + 1
		x3 = (x1 + x2)/2
		if calculo(x3)*calculo(x1) < 0:
			x2 = x3
		else: 
			x1 = x3
	return (x1,x2,x3,iter)
		

print(bisseccao(0.5, 3, 1000, 10e-6))
