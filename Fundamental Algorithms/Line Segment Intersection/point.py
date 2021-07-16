import numpy as np
import pylab as pl
import random
from matplotlib import collections  as mc

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        return False

    def __sub__(self, other):
        xd = self.x - other.x
        yd = self.y - other.y
        res = Point(xd,yd)
        return res

    def __add__(self, other):
        xd = self.x + other.x
        yd = self.y + other.y
        res = Point(xd,yd)
        return res

    def cross_product(self, pt):

        m1 = self.x*pt.y
        m2 = self.y*pt.x
        return m1-m2

    def dot_product(self, pt):

        return (self.x*pt.x) + (self.y*pt.y)

    def scale(self, factor):

        xsc = self.x*factor
        ysc = self.y*factor
        res = Point(xsc, ysc)
        return res


class LineSegment:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return "({},{})<--->({},{})".format(self.p.x,self.p.y,self.q.x,self.q.y)

    def orientation(self,r):

        t1 = (self.q.x - self.p.x)*(r.y - self.p.y)
        t2 = (self.q.y - self.p.y)*(r.x - self.p.x)
        C = t1 - t2

        if C<0: #clockwise order of p,q,r
            return 1
        elif C==0: #collinear
            return 0
        else: #anti-clockwise
            return -1

def plot_intersegments(S,P):

    lines = []
    xs = []
    ys = []

    for seg in S:
        arr = [(seg.p.x, seg.p.y), (seg.q.x, seg.q.y)]
        lines.append(arr)

    for point in P:
        xs.append(point.x)
        ys.append(point.y)

    lc = mc.LineCollection(lines, linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.scatter(xs,ys,c="r")
    ax.autoscale()
    ax.margins(0.1)
    ax.set_title("Line Segment Intersection")

    num = random.randint(1, 10)

    fig.savefig("LinSegInt" + str(num) + ".png")
