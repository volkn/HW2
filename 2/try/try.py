import matplotlib.pyplot as plt 
import numpy as np 

rng = np.random.RandomState()
X1 = 5 * rng.rand(50)
Y = 2 * X1 - 5 + rng.randn(50)

def theta(x, y):
    m = np.size(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    line_y = np.sum(y*x - m*mean_y*mean_x)
    line_x = np.sum(x*x - m*mean_x*mean_x)
    theta1 = line_y / line_x
    theta0 = mean_y - theta1*mean_x

    return(theta0,theta1)

def regression(x,y,theta):
    plt.scatter(x,y)
    regressio_line = theta[0]+theta[1]*x
    plt.plot(x,regressio_line)
    plt.show()

    
theta = theta(X1,Y)
print("theta0 = {}, theta1 = {}".format(theta[0],theta[1]))
regression(X1, Y, theta)
