import numpy as np

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

    def distance(self, other):

        vec = self - other
        return np.sqrt((vec.x**2) + (vec.y**2))


class Segment:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return "({},{})==({},{})".format(self.p.x,self.p.y,self.q.x,self.q.y)

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
