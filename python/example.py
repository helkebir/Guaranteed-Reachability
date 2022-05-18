from bihari import *
from geometry_tools import *

if __name__ == "__main__":
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    original = read_polygon('example.txt')
    impaired = read_polygon('example_impaired.txt')

    m = 5
    c = 0.2
    k = 0.5
    alf = 0.1

    norm = 0.1498
    tf = 0.1
    eps = 0.25

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : x + (1/m)*(u + k*x + alf*x**3 + c*x + 3*alf*(x*x*norm + x*norm*norm))

    dh = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)(0, tf)

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
    ax.set_title("Duffing Oscillator Reachable Set @ $t = 0.1$ s")

    plt.show()