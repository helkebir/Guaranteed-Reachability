from bihari import *
from geometry_tools import *
import numpy as np
import scipy.integrate
import skgeom as sg
from skgeom import boolean_set, minkowski
from skgeom.draw import draw

def generateRectangle(xmin, xmax, ymin, ymax):
    return np.asarray([[xmin,ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]])

if __name__ == "__main__":
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    original = read_polygon('norrbin_t500.txt')
    impaired = read_polygon('norrbin2_t500.txt')

    v = 5
    l = 45
    umax = np.deg2rad(25)
    gamma = v/l

    X2 = 0.0862
    tf = 0.5
    eps = 0.2*np.deg2rad(25)

    a = lambda t : 1
    b = lambda t : 0
    w = lambda x, u : 0.5*gamma*(x + x*x*x + 3*x*x*X2 + 3*x*X2*X2) + 0.5*gamma*gamma*u

    dh_func = bihari(a, w, b, eps, r0=1e-3, tol=1e-9)
    f = lambda t : dh_func(0, t)
    # dh = tf*f(tf)
    dh2 = f(tf)

    print(dh2)
    dh1 = scipy.integrate.quad(f, 0, tf)[0]
    print(dh1, tf*dh2)
    dh = max(dh1, dh2)

    x, y, xs, ys = shrink(original, dh)
    r = 1e-6
    _, _, xInner, yInner = shrink(original, r)
    _, _, xOuter, yOuter = shrink(original, -r)

    rect = generateRectangle(-dh1, dh1, -dh2, dh2)

    poly = sg.Polygon([sg.Point2(p[0], p[1]) for p in np.vstack([x, y]).T])
    poly_shrunk = sg.Polygon([sg.Point2(p[0], p[1]) for p in np.vstack([xs, ys]).T])
    poly_rect = sg.Polygon([sg.Point2(p[0], p[1]) for p in rect])

    poly_inner = sg.Polygon([sg.Point2(p[0], p[1]) for p in np.vstack([xInner, yInner]).T[:-1]])
    # print(np.vstack([xInner, yInner]).T)
    poly_outer = sg.Polygon([sg.Point2(p[0], p[1]) for p in np.vstack([xOuter, yOuter]).T[:-1]])

    shapelyPolyInner = geometry.Polygon(np.vstack([xInner, yInner]).T).buffer(0)
    shapelyPolyOuter = geometry.Polygon(np.vstack([xOuter, yOuter]).T).buffer(0)
    # shapelyPolyOuter.difference(shapelyPolyInner)

    bd = geometry.Polygon(np.vstack([xOuter, yOuter]).T[:-1], [np.vstack([xInner, yInner]).T[:-1][::-1]])

    bdOuter = sg.Polygon([sg.Point2(p[0], p[1]) for p in np.vstack([xOuter, yOuter]).T[:-1][::-1]])
    bdInner = sg.Polygon([sg.Point2(p[0], p[1]) for p in np.vstack([xInner, yInner]).T[:-1]])

    bdPoly = sg.PolygonWithHoles(bdOuter, [bdInner])

    # x,y = bd.exterior.xy
    # print(np.vstack([x, y]).T)
    # plt.plot(x,y)
    # x,y = bd.interiors[0].xy
    # plt.plot(x,y)

    # draw(bdPoly)

    bdPolyFattened = minkowski.minkowski_sum(bdOuter, poly_rect)

    print(bdPolyFattened.outer_boundary().coords[:,0])

    draw(bdPolyFattened)
    draw(bdOuter)

    # draw(poly)
    # draw(poly_shrunk)
    # draw(poly_outer)
    # draw(poly_inner)
    # draw(sg.PolygonWithHoles(poly_outer, [poly_inner]))
    # draw(boolean_set.difference(poly_outer, poly_inner))
    # draw(poly_rect)
    # poly = sg.Polygon([sg.Point2(0, 0), sg.Point2(0, 3), sg.Point2(3, 3)])

    # hole = sg.Polygon([
    #     sg.Point2(1.0, 2.0),
    #     sg.Point2(1.0, 2.5),
    #     sg.Point2(0.5, 2.5),
    #     sg.Point2(0.5, 2.0)]
    # )
    # poly_with_hole = sg.PolygonWithHoles(poly, [hole])
    # draw(poly_with_hole)
    
    plt.show()
