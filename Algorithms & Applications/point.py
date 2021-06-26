import matplotlib.pyplot as plt

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

class DirectedEdge:

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __str__(self):
        return "({},{})=>({},{})".format(self.p.x,self.p.y,self.q.x,self.q.y)

    def is_r_left_of_pq(self,r):

        t1 = (self.q.x - self.p.x)*(r.y - self.p.y)
        t2 = (self.q.y - self.p.y)*(r.x - self.p.x)
        C = t1 - t2

        if C>0:
            return True
        return False

def clockwise_verts(E):

    L = list()
    e = E[0]
    L.append(e.p)

    crind = 0

    while(len(E)>1):
        del E[crind]
        d = e.q
        L.append(d)

        for i in range(0,len(E)):
            if E[i].p == d:
                e = E[i]
                crind = i
                break
    return L

def plot_polygon(P, L, title):

    xs = []
    ys = []

    for point in P:
        xs.append(point.x)
        ys.append(point.y)

    lx = []
    ly = []

    for i in range(0,len(L)):
        lx.append(L[i].x)
        ly.append(L[i].y)

    lx.append(L[0].x)
    ly.append(L[0].y)

    plt.scatter(xs, ys, c="r")
    plt.plot(lx,ly)
    plt.title(title)
    plt.savefig(title+".png")
    plt.close()
