import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib 
from sympy import * 

rng = np.random.RandomState(1)
list_x = 5 * rng.rand(50)
list_y = 2 * list_x - 5 + rng.randn(50)
#print(list_x)
#print(list_y)
line_tuples_list = []

line_y = []
#x = Symbol('x')
#y = Symbol('y')
m = Symbol('m')
n = Symbol('n')

line_y = []
y = 0
for i in list_x:
    y = m * i + n
    line_y.append(y)
    y = 0

line_y = np.array(line_y)

distances = list_y - line_y
print(distances)
#print(list_y)
a = 0
for i in distances:
    a += i
print(a)

#print(line_y)
#print(line_y)
plt.scatter(list_x, list_y)
plt.show()
