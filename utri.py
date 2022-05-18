from bihari import *
from geometry_tools import *
import numpy as np
import scipy.integrate

if __name__ == "__main__":
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    original = read_polygon('utri12_t1000.txt')
    impaired = read_polygon('utriimp12_t1000.txt')

    v = 5
    l = 45
    umax = np.deg2rad(25)
    gamma = v/l

    X2 = 0.0862
    tf = 1.0
    eps = 0.2

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : x + (1+2+3+4)*eps/8

    dh1_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f1 = lambda t : dh1_func(0, t)
    dh1 = 0.4295511490333736

    print("dh1", dh1)

    a = lambda t : 1
    b = lambda t : (1/2)*dh1
    w = lambda x, u : x + (1+2+3+4)*eps/7

    dh2_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f2 = lambda t : dh2_func(0, t)
    dh2 = 0.7349687532610415

    print("dh2", dh2)

    a = lambda t : 1
    b = lambda t : (1/3)*dh1 + (2/3)*dh2
    w = lambda x, u : x + (1+2+3+4)*eps/6

    dh3_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f3 = lambda t : dh3_func(0, t)
    dh3 = 1.2151426033100305

    print("dh3", dh3)

    a = lambda t : 1
    b = lambda t : (1/4)*dh1 + (2/4)*dh2 + (3/4)*dh3
    w = lambda x, u : x + (1+2+3+4)*eps/5

    dh4_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f4 = lambda t : dh4_func(0, t)
    dh4 = 1.9611368166359813

    print("dh4", dh4)

    a = lambda t : 1
    b = lambda t : (1/5)*dh1 + (2/5)*dh2 + (3/5)*dh3 + (4/5)*dh4
    w = lambda x, u : x + (1+2+3+4)*eps/4

    dh5_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f5 = lambda t : dh5_func(0, t)
    dh5 = 3.1164069508602164

    print("dh5", dh5)

    a = lambda t : 1
    b = lambda t : (1/6)*dh1 + (2/6)*dh2 + (3/6)*dh3 + (4/6)*dh4 + (5/6)*dh5
    w = lambda x, u : x + (1+2+3+4)*eps/3

    dh6_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f6 = lambda t : dh6_func(0, t)
    dh6 = f6(tf)

    print("dh6", dh6)

    a = lambda t : 1
    b = lambda t : (1/7)*dh1 + (2/7)*dh2 + (3/7)*dh3 + (4/7)*dh4 + (5/7)*dh5 + (6/7)*dh6
    w = lambda x, u : x + (1+2+3+4)*eps/2

    dh7_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f7 = lambda t : dh7_func(0, t)
    dh7 = f7(tf)

    print("dh7", dh7)

    a = lambda t : 1
    b = lambda t : (1/8)*dh1 + (2/8)*dh2 + (3/8)*dh3 + (4/8)*dh4 + (5/8)*dh5 + (6/8)*dh6 + (7/8)*dh7
    w = lambda x, u : x + (1+2+3+4)*eps

    dh8_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f8 = lambda t : dh8_func(0, t)
    dh8 = f8(tf)

    print("dh8", dh8)

    dh = np.sqrt(dh1**2 + dh2**2)
    # dh = np.sqrt(dh1**2 + dh2**2 + dh3**2 + dh4**2 + dh5**2 + dh6**2 + dh7**2 + dh8**2)
    print(dh)
    print(dh1, dh2, dh3, dh4, dh5, dh6, dh7, dh8)

    x, y, xs, ys = shrink(original, dh)

    # x, y, xs1, ys1 = shrink(original, dh1)
    # x, y, xs2, ys2 = shrink(original, dh2)

    mpl.rcParams['font.size'] = 10

    ax = plt.subplot()
    ax.grid(which='major', alpha=0.5, color='k')
    ax.grid(which='minor', alpha=0.3, color='k', linestyle=':')
    ax.minorticks_on()
    ax.set_axisbelow(True)

    ax.fill(x, y, color='b', facecolor='lightskyblue',
        edgecolor='dodgerblue', label='Nominal', alpha=0.75)
    ax.fill(impaired[:,0], impaired[:,1], facecolor='lightsalmon',
        edgecolor='orangered', label='Off-nominal', alpha=0.75)
    
    # ax.fill(xs1, ys1, facecolor='none', edgecolor='rebeccapurple',
    #     label='Approx. $x_1$', hatch='////', alpha=1)

    # ax.fill(xs2, ys2, facecolor='none', edgecolor='rebeccapurple',
    #     label='Approx. $x_2$', hatch="\\\\\\", alpha=1)

    ax.fill(xs, ys, facecolor='mediumseagreen', edgecolor='forestgreen',
        label='Inner approx.', alpha=0.75)

    ax.set_aspect('equal')
    # ax.legend()

    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_title("Lower Triangular Diminished Authority \n Reachable Set @ $t = 1$ s")

    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    plt.tight_layout()
    # plt.savefig("norrbinDiminished500.pdf", bbox_inches = 'tight',
    # pad_inches = 0)

    plt.show()