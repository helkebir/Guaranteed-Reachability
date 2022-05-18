import numpy as np
from scipy.optimize import newton, brentq, root_scalar
from scipy.integrate import RK45, solve_ivp

# Type hints
from collections.abc import Callable
from typing import Union

def bihari(a: Callable[[float], float],
    w: Callable[[float, float], float], b: Callable[[float], float],
    eps: float, r0: float = 0.1, tol: float = 1e-3, x0: float = 1e-9,
    debug: bool = False) -> Callable[[float, float], float]:
    """Returns a solver for the Bihari inequality.

    In our setting, the Bihari equation applies to the following
    inequality, where `f(t, x, u) = xdot(t)` defines the dynamics of the
    nominal system.

    `|f(t, x + xb, u + ub) - f(t, x, u)| <= a(t) * w(|xb|, |ub|) + b(t)`

    Args:
        a: A nonnegative nondecreasing function of time.
        b: A nonnegative nondecreasing function of time.
        c: A nonnegative function, nondecreasing in both `xb` and `ub`.
        eps: A float denoting the maximum norm of `ub`.
        r0: A positive float, best taken to be small.
        tol: Absolute convergence tolerance for the root finding scheme.
        x0: First guess for G inverse root finding, best taken small.
        debug: If true, returns internal functions as well.

    Returns:
        A lambda function taking arguments of initial and final time,
        either returning a float or a list of floats.

        If debug is true, this list of floats contains
        `Ginv(G(...)), G(...), G, Ginv` as functions of `(t0, t)`.
    """
    G = lambda _r0, _r : solve_ivp(lambda t, y : np.asarray([1/w(t,eps)], dtype=np.double), (_r0, _r), np.asarray([0])).y[0,-1]
    Ginv = lambda _G0 : root_scalar(lambda _r : (G(r0, _r) - _G0), x0=x0, x1=2*x0, xtol=tol, method='secant').root
    
    if debug:
        return lambda t0, t : (
            Ginv(G(r0, solve_ivp(lambda _t, _y : np.asarray([b(_t)], dtype=np.double), (t0, t), np.asarray([0])).y[0,-1]) + solve_ivp(lambda _t, _y : np.asarray([a(_t)], dtype=np.double), (t0, t), np.asarray([0])).y[0,-1]),
            G(r0, solve_ivp(lambda _t, _y : np.asarray([b(_t)], dtype=np.double), (t0, t), np.asarray([0])).y[0,-1]) + solve_ivp(lambda _t, _y : np.asarray([a(_t)], dtype=np.double), (t0, t), np.asarray([0])).y[0,-1],
            G,
            Ginv
        )
    else:
        return lambda t0, t : Ginv(G(r0, solve_ivp(lambda _t, _y : np.asarray([b(_t)], dtype=np.double), (t0, t), np.asarray([0])).y[0,-1]) + solve_ivp(lambda _t, _y : np.asarray([a(_t)], dtype=np.double), (t0, t), np.asarray([0])).y[0,-1])

if __name__ == "__main__":
    norm = 0.4159
    tf = 0.35
    eps = 0.02

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : 4*x + 10*norm*x + 5*x*x + 2*u

    golden = 0.0834069157119783

    assert(np.isclose(bihari(a, w, b, eps, r0=1e-29, tol=1e-9)(0, tf), golden))
    print("SUCCESS")