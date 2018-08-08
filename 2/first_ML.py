import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib 


rng = np.random.RandomState(1)
X = np.array(list(map(lambda x: [5*x], rng.rand(50))))
y = np.array(list(map(lambda x: (x[0]*0.4+rng.rand(1))[0], X)))

m=len(X)
bias=1.1
theta=np.array([1.1])
def h(Xi):
    return np.matmul(theta, np.transpose(Xi))+bias

def J(derivate=False,alfa=0,thetai=0):
    sum=0
    if(derivate):
        if(thetai==0):
            for i in range(m):
                sum+=(h(X[i])-y[i])
        else:
            for i in range(m):
                sum+=(h(X[i])-y[i])*X[i][thetai-1]
        return alfa*(sum/m)
    else:
        for i in range(m):
            sum+=(h(X[i])-y[i])**2
        return sum/(2*m)

def gradient_descent():
    global bias,theta
    alfa = 0.001
    for i in range(7000):
        bias = bias - J(derivate=True,alfa=alfa,thetai=0)
        for k in range(len(theta)):
            theta[k] = theta[k] - J(derivate=True,alfa=alfa,thetai=k+1)
            if(i%200==0):
                print("cost: ",J(derivate=False))

gradient_descent()

print("theta,bias: ",theta,bias)

plt.scatter(X, y)
plt.plot([0,6],[h([0]),h([6])],"r")

plt.show()
