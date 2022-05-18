from bihari import *
from geometry_tools import *
import numpy as np
import scipy.integrate

if __name__ == "__main__":
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    original = read_polygon('norrbin_t5000.txt')
    impaired = read_polygon('norrbin2_t5000.txt')

    v = 5
    l = 45
    umax = np.deg2rad(25)
    gamma = v/l

    X2 = 0.0777
    tf = 5
    eps = 0.2*np.deg2rad(25)

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : 0.5*gamma*(x + x*x*x + 3*x*x*X2 + 3*x*X2*X2) + 0.5*gamma*gamma*u

    dh_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f = lambda t : dh_func(0, t)
    dh = 5*f(tf)

    print(scipy.integrate.quad(f, 0, tf)[0], tf*f(tf))

    x, y, xs, ys = shrink(original, dh)

    ax = plt.subplot()
    ax.grid(which='major', alpha=0.5, color='k')
    ax.grid(which='minor', alpha=0.3, color='k', linestyle=':')
    ax.minorticks_on()
    ax.set_axisbelow(True)

    ax.fill(x, y, color='b', facecolor='lightskyblue',
        edgecolor='dodgerblue', label='Nominal', alpha=0.75)
    ax.fill(impaired[:,0], impaired[:,1], facecolor='lightsalmon',
        edgecolor='orangered', label='Off-nominal', alpha=0.75)
    ax.fill(xs, ys, facecolor='mediumseagreen', edgecolor='forestgreen',
        label='Inner approx.', alpha=0.75)
    ax.set_aspect('equal')
    ax.legend()

    ax.set_xlabel('Position [m]')
    ax.set_ylabel('Velocity [m/s]')
    ax.set_title("Norrbin Reachable Set @ $t = 0.5$ s")

    plt.show()