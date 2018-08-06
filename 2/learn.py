import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib


rng = np.random.RandomState(1)
X = np.array(list(map(lambda x: [5*x], rng.rand(50))))
Y = np.array(list(map(lambda x: (x[0]*0.4+rng.rand(1))[0], X)))


#print(X)
print(X.transpose())
#print(Y)

bias = 1
theta1 = 1

theta = np.array([theta1])
#print(theta)

def h(x):
    return (bias + np.matmul(theta,x.transpose()))

#print(h(X))
#print(h(X).transpose())

def J(gradient=False, alfa=0.01, bias_=0):
    global theta, bias, X, Y, theta1
    m = len(X)
    if gradient == True:
        if bias_ == 0:
            for i in range(100000):
                inner = h(X) - Y 
                inner = np.sum(inner)
                bias = bias - alfa * (1.0/m) * inner
            return bias
        else:
            for i in range(100000):
                a = h(X)
                inner = np.matmul(a - Y, X)
                inner = np.sum(inner)
                theta1 = theta1 - alfa * (1.0/m) * inner
            return theta1
    else:
        inner = np.power((X @ theta.T) - Y, 2) 
        J = (np.sum(inner) + len(X)*bias) / 2 * len(X)
        return J


print(J())
J(gradient=True, bias_=0)
J(gradient=True, bias_=1)
print(J())
#print(h(X))

plt.scatter(X, Y)
#plt.scatter(h(X), Y)
plt.show()
