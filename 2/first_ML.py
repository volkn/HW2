import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib 
from sympy import * 

rng = np.random.RandomState()
X1 = 5 * rng.rand(50)
Y = 2 * X1 - 5 + rng.randn(50)
#print(X1)
#print(Y)
line_tuples_list = []

#x = Symbol('x')
#y = Symbol('y')
theta0 = Symbol('m')
theta1 = Symbol('n')

h_X1 = []
y = 0
for i in X1:
    y = theta0 * i + theta1
    h_X1.append(y)
    y = 0

h_X1 = np.array(h_X1)


distances = []

for i in range(len(h_X1)):
    distances.append((h_X1[i] - Y[i])**2)
#print(distances)

distances = np.array(distances)

#distances = Y - h_X1
#print(distances)

J = 0
for i in distances:
    J += i

J = J / (2*theta0)
print(J)
#print(line_y)
#print(line_y)
plt.scatter(X1, Y)
plt.show()
