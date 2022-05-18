from bihari import *
from geometry_tools import *
import numpy as np
import scipy.integrate

if __name__ == "__main__":
    tf = 0.25
    eps = 0.1

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : (1 + 1 + 1) * x + 1.1*eps

    dh1_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f1 = lambda t : dh1_func(0, t)
    dh1 = f1(tf)

    print("dh1", dh1)

    a = lambda t : 1
    b = lambda t : (0.1 + 0.5)*f1(t)
    w = lambda x, u : (0.5 + 0.1 + 0.5 + 1 + 0.1 + 0.5 + 0.5 + 0.1)*x + 0.3*eps

    dh2_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f2 = lambda t : dh2_func(0, t)
    dh2 = f2(tf)

    print("dh2", dh2)
    print("\n"*20)