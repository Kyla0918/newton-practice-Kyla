import numdifftools as nd
import numpy as np

def multinewton(f,x0):
    x1 = x0
    grad = nd.Gradient(f)
    hess = nd.Hessian(f)
    while abs(x1 - x0) > 0.0001:
        x1 = x0 - np.linalg.inv(hess(x0)) * grad(x0)
    return x1