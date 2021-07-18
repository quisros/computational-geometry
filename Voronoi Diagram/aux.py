from point import *
import numpy as np
import pylab as pl
import random
from matplotlib import collections  as mc

def BoundingBox(P):

    crt_x_min = P[0].x
    crt_x_max = P[0].x

    crt_y_min = P[0].y
    crt_y_max = P[0].y

    for point in P:
        if point.x > crt_x_max:
            crt_x_max = point.x
        if point.x < crt_x_min:
            crt_x_min = point.x
        if point.y > crt_y_max:
            crt_y_max = point.y
        if point.y < crt_y_min:
            crt_y_min = point.y

    lower_left = Point(crt_x_min-3, crt_y_min-3)
    upper_rght = Point(crt_x_max+3, crt_y_max+3)

    return (lower_left, upper_rght)

def plot_voronoi(P,S):

    (ll, ur) = BoundingBox(P)

    xs = []
    ys = []
    for point in P:
        xs.append(point.x)
        ys.append(point.y)

    lines = []
    for seg in S:
        arr = [(seg.p.x, seg.p.y), (seg.q.x, seg.q.y)]
        lines.append(arr)

    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.scatter(xs,ys,c="r")
    ax.autoscale()
    ax.margins(0.1)
    ax.set_title("Voronoi Diagram")

    ax.set_xlim(ll.x, ur.x)
    ax.set_ylim(ll.y, ur.y)

    ax.grid(True)

    num = random.randint(1, 10)

    fig.savefig("VoronoiDiag" + str(num) + ".png")
