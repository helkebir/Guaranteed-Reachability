from bihari import *
from geometry_tools import *
import numpy as np
import scipy.integrate

if __name__ == "__main__":
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    original = read_polygon('norrbin_t1000.txt')
    impaired = read_polygon('norrbin3_t1000.txt')

    v = 5
    v2 = 4.75
    l = 45
    umax = np.deg2rad(25)
    gamma = v/l
    gamma2 = v2/l

    X2min = 0.0799
    X2 = 0.0851
    tf = 1
    eps = 0.2*np.deg2rad(25)

    a = lambda t : 1
    b = lambda t : 0.5*abs(gamma2 - gamma)*(X2min + X2min**3) + 0.5*(gamma*gamma - gamma2*gamma2) * umax
    # b = lambda t : 0.5*abs(gamma2 - gamma)*(X2 + X2**3) + 0.5*(gamma*gamma - gamma2*gamma2) * umax
    w = lambda x, u : 0.5*gamma*(x + x*x*x + 3*x*x*X2 + 3*x*X2*X2) + 0.5*gamma*gamma*u

    dh_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f = lambda t : dh_func(0, t)
    # dh = tf*f(tf)
    dh2 = f(tf)

    print(dh2)
    dh1 = scipy.integrate.quad(f, 0, tf)[0]
    print(dh1, tf*dh2)
    # dh = max(dh1, dh2)
    dh = np.sqrt(dh1**2 + dh2**2)

    x, y, xs, ys = shrink(original, dh)

    x, y, xs1, ys1 = shrink(original, dh1)
    x, y, xs2, ys2 = shrink(original, dh2)

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

    plt.axvspan(min(xs1), max(xs1), facecolor='none', edgecolor='rebeccapurple',
        alpha=1)

    plt.axvspan(min(xs1), max(xs1), facecolor='none', edgecolor='rebeccapurple',
        label='Guaranteed $x_1$', hatch='////', alpha=0.5)

    # ax.fill(xs2, ys2, facecolor='none', edgecolor='rebeccapurple',
    #     label='Approx. $x_2$', hatch="\\\\\\", alpha=1)

    plt.axhspan(min(ys2), max(ys2), facecolor='none', edgecolor='rebeccapurple',
        alpha=1)

    plt.axhspan(min(ys2), max(ys2), facecolor='none', edgecolor='rebeccapurple',
        label='Guaranteed $x_2$', hatch="\\\\\\", alpha=0.5)

    ax.fill(xs, ys, facecolor='mediumseagreen', edgecolor='forestgreen',
        label='Inner approx.', alpha=0.75)

    ax.set_aspect('equal')
    ax.legend()

    ax.set_xlabel('Heading [rad]')
    ax.set_ylabel('Heading rate [rad/s]')
    ax.set_title("Norrbin Slowdown Reachable Set @ $t = 1$ s")

    plt.tight_layout()
    plt.savefig("norrbinSlowdown.pdf", bbox_inches = 'tight',
    pad_inches = 0)

    plt.show()