from bihari import *
from geometry_tools import *
import numpy as np
import scipy.integrate

if __name__ == "__main__":
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    original = read_polygon('utri12_t250.txt')
    impaired = read_polygon('utriimp12_t250.txt')

    v = 5
    l = 45
    umax = np.deg2rad(25)
    gamma = v/l

    X2 = 0.0862
    tf = 0.25
    eps = 0.1

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : x + (1+2+3+4)*eps/8

    dh1_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f1 = lambda t : dh1_func(0, t)
    dh1 = f1(tf)

    print("dh1", dh1)

    a = lambda t : 1
    b = lambda t : (1/2)*f1(t)
    w = lambda x, u : x + (1+2+3+4)*eps/7

    dh2_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f2 = lambda t : dh2_func(0, t)
    dh2 = f2(tf)

    print("dh2", dh2)

    a = lambda t : 1
    b = lambda t : (1/3)*f1(t) + (2/3)*f2(t)
    w = lambda x, u : x + (1+2+3+4)*eps/6

    dh3_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f3 = lambda t : dh3_func(0, t)
    dh3 = f3(tf)

    print("dh3", dh3)

    a = lambda t : 1
    b = lambda t : (1/4)*f1(t) + (2/4)*f2(t) + (3/4)*f3(t)
    w = lambda x, u : x + (1+2+3+4)*eps/5

    dh4_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f4 = lambda t : dh4_func(0, t)
    dh4 = f4(tf)

    print("dh4", dh4)

    a = lambda t : 1
    b = lambda t : (1/5)*f1(t) + (2/5)*f2(t) + (3/5)*f3(t) + (4/5)*f4(t)
    w = lambda x, u : x + (1+2+3+4)*eps/4

    dh5_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f5 = lambda t : dh5_func(0, t)
    dh5 = f5(tf)

    print("dh5", dh5)

    a = lambda t : 1
    b = lambda t : (1/6)*f1(t) + (2/6)*f2(t) + (3/6)*f3(t) + (4/6)*f4(t) + (5/6)*f5(t)
    w = lambda x, u : x + (1+2+3+4)*eps/3

    dh6_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f6 = lambda t : dh6_func(0, t)
    dh6 = f6(tf)

    print("dh6", dh6)

    a = lambda t : 1
    b = lambda t : (1/7)*f1(t) + (2/7)*f2(t) + (3/7)*f3(t) + (4/7)*f4(t) + (5/7)*f5(t) + (6/7)*f6(t)
    w = lambda x, u : x + (1+2+3+4)*eps/2

    dh7_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f7 = lambda t : dh7_func(0, t)
    dh7 = f7(tf)

    print("dh7", dh7)

    a = lambda t : 1
    b = lambda t : (1/8)*f1(t) + (2/8)*f2(t) + (3/8)*f3(t) + (4/8)*f4(t) + (5/8)*f5(t) + (6/8)*f6(t) + (7/8)*f7(t)
    w = lambda x, u : x + (1+2+3+4)*eps

    dh8_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f8 = lambda t : dh8_func(0, t)
    dh8 = f8(tf)

    print("dh8", dh8)

    dh = np.sqrt(dh1**2 + dh2**2 + dh3**2 + dh4**2 + dh5**2 + dh6**2 + dh7**2 + dh8**2)
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

    ax.set_xlabel('Heading [rad]')
    ax.set_ylabel('Heading rate [rad/s]')
    ax.set_title("Lower Triangular Diminished Authority \n Reachable Set @ $t = 1$ s")

    plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    plt.tight_layout()
    # plt.savefig("norrbinDiminished500.pdf", bbox_inches = 'tight',
    # pad_inches = 0)

    plt.show()