
e = 0.0001

def f(x):
    y = x*x + 2*x + 1
    return y

def fderi(x):
    e = 0.0001
    y = (f(x+e)-f(x))/e
    return(y)

def fderi2(x):
    e = 0.0001
    y = (fderi(x+e)-fderi(x))/e
    return(y)

def optimize(x0):
    x1 = x0
    while abs(x0-x1) < 0.0001:
        x1 = x0 - fderi(x0)/fderi2(x0)
