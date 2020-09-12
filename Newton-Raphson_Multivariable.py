"""
Program to solve a system of differential 
non-linear coupled equations

	dy1/dt = -0.04*y1 + 10^4*y2*y3
	dy2/dt = 0.04*y1 - 10^4*y2*y3 -3*10^7*y2^2
	dy3/dt = 3*10^7*y2^2

# We will use a BDF using Multivariate Newton Raphson Method

	f1 = y1(n-1) + dt*(-0.04*y1(n) + 10^4*y2(n)*y3(n)) - y1(n) = 0
	f2 = y2(n-1) + dt*(0.04*y1(n)-10^4*y2(n)*y3(n)-3*10^7*y2(n)^2) - y2(n) = 0
	f3 = y3(n-1) + dt*(3*10^7*y2(n)^2) - y3(n) = 0

"""
import math
import numpy as np 
from numpy.linalg import inv
import matplotlib.pyplot as plt 

#Problem Parameters
a1 = -0.04
a2 = 1e4
a3 = 3e7

#Variables for the time loop
dt=0.05
t_final = 10*60
t_initial = 0


def f1(y1_old,y1,y2,y3,dt):
	return y1_old + dt*(a1*y1 + a2*y2*y3) - y1

def f2(y2_old,y1,y2,y3,dt):
	return y2_old + dt*(-a1*y1-a2*y2*y3-a3*y2**2) - y2

def f3(y3_old,y1,y2,y3,dt):
	return y3_old + dt*(a3*y2**2) - y3

def jacobian(y1,y2,y3,dt):
	J = np.ones((3,3))

	#Row 1
	J[0,0] = -0.04*dt - 1
	J[0,1] = 10**4*y3
	J[0,2] = 10**4*y2

	#Row 2
	J[1,0] = 0.04*dt 
	J[1,1] = dt*(-10**4*y3 - 6*10**7*y2) - 1
	J[1,2] = dt*(-10**4*y2)

	#Row 3
	J[2,0] = 0
	J[2,1] = dt*(6*10**7*y2)
	J[2,2] = -1

	return J

#Defining the initial and guess values
y1 = 1
y2 = 0
y3 = 0
#numpy column vector
Y_old = np.ones((3,1))
#numpy column vector
Y_guess = np.ones((3,1))

#numpy time vector
t = np.arange(t_initial,t_final,dt)
total_iter = len(t)

#numpy solution matrix
Y = np.ones((3,total_iter))

#numpy column vecotr for F
F = np.copy(Y_guess)

#Starting the Time integration Loop
time_iter = 0

for i in range(1,total_iter+1):

	Y_old[0] = y1
	Y_old[1] = y2
	Y_old[2] = y3

	Y_guess[0] = y1
	Y_guess[1] = y2
	Y_guess[2] = y3
	
	#Parameters for Newton Raphson solver
	error = 9e9  #Initializing error
	alpha = 1
	tol = 1e-8

	#Starting the Newton Raphson loop
	iter = 1

	while error > tol:

		#Computing the F vector - old values are used
		F[0] = f1(Y_old[0], Y_guess [0], Y_guess[1], Y_guess[2], dt)
		F[1] = f2(Y_old[1], Y_guess [0], Y_guess[1], Y_guess[2], dt)
		F[2] = f3(Y_old[2], Y_guess [0], Y_guess[1], Y_guess[2], dt)

		#Computed the Analytical Jacobian  - old values are used
		J = jacobian(Y_guess[0], Y_guess[1], Y_guess[2], dt)
		#print(J)

		# Computing the Numerical Jacobian
		n=len(Y_guess)
		eps = 1e-8
		Y_perturb = np.copy(Y_guess)
		F_perturb = np.zeros((3,1))
		Jac = np.zeros((3,3))
		k=0
		for i in range(n):

			Y_perturb[i] = Y_guess[i] + eps
			F_perturb[0] = f1(Y_old[0], Y_perturb[0], Y_perturb[1], Y_perturb[2], dt)
			F_perturb[1] = f2(Y_old[1], Y_perturb[0], Y_perturb[1], Y_perturb[2], dt)
			F_perturb[2] = f3(Y_old[2], Y_perturb[0], Y_perturb[1], Y_perturb[2], dt)
			Jac[0,i] = (F_perturb[0] - F[0])/eps
			Jac[1,i] = (F_perturb[1] - F[1])/eps
			Jac[2,i] = (F_perturb[2] - F[2])/eps
			#print(X_perturb)
			Y_perturb[i] = Y_guess [i]
		#print(Jac)

		#Computing the new values
		Y_new = Y_guess - alpha*np.matmul(inv(Jac),F)

		#Computing max abs error
		error = np.max(np.abs(Y_new-Y_guess))

		#Updating old values 
		Y_guess = Y_new

		#log message
		log_message = 'iteration # = {0} y1={1} y2={2} y3={3}' .format(iter,Y_new[0],Y_new[1],Y_new[2])
		print(log_message)
		iter = iter + 1

	#Final results
	y1 = Y_new[0]
	y2 = Y_new[1]
	y3 = Y_new[2]

	Y[0,time_iter]= Y_new[0]
	Y[1,time_iter]= Y_new[1]
	Y[2,time_iter]= Y_new[2]

	time_iter = time_iter + 1 

#Make sure the size of the matrix and time vector corresponds
size = np.shape(Y)
print(size)
print(total_iter)

plt.plot(t,Y[0,:],color='black')
plt.plot(t,Y[1,:],color='orange')
plt.plot(t,Y[2,:],color='blue')
plt.legend(['Y1','Y2','Y3'])
plt.show()




'''
S. (2020). Multivariate Newton-Raphson method : Skill-Lync. Skill. 
https://skill-lync.com/projects/Multivariate-Newton-Raphson-method-23645
'''