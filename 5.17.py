from gaussxw import gaussxw
import numpy
from numpy import sqrt, e, linspace, exp, log
import matplotlib
import matplotlib.pyplot as plt

N = 100 #number of slices
#limits of the integral
a = 0 
b = 1

x,w = gaussxw(N)

xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w
def f(x):
    return x**(n-1)* exp(-x)
#substitute x=z/1-z and change the limits
def gamma(a,z):
    c=a-1
    def F(z):
        return  c*(exp(c * log((c * z) / (1 - z)) - (c*z) / (1 - z)) )*(1/(1-z)**2)
#perform the integration
    s = 0.0
    for k in range(N):
        s += wp[k]*F(xp[k])
    return s
    


z=numpy.linspace(0,5)
g=[gamma(2,z) for zi in z]
plt.plot(z, g)
plt.show()
