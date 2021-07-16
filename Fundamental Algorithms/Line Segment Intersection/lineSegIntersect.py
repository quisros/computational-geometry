import sys
import random
from point import *

def IntervalOverlap(a, b):

    c1 = (a<=0 and 0<=b) or (a<=1 and 1<=b)
    c2 = (0<=a and a<=1) and (0<=b and b<=1)

    if c1 or c2: return True
    return False


def PairIntersection(sl, sr):

    p = sl.p
    r = sl.q - sl.p

    q = sr.p
    s = sr.q - sr.p

    check1 = r.cross_product(s)
    check2 = (q-p).cross_product(r)

    if check1==0:
        if check2==0:
            t0 = ((q-p).dot_product(r)) / r.dot_product(r)
            t1 = t0 + (s.dot_product(r) / r.dot_product(r))
            if IntervalOverlap(t0,t1) or IntervalOverlap(t1, t0):
                return sr.p
            else:
                return None
        else:
            return None

    else:
        t = (q-p).cross_product(s) / r.cross_product(s)
        u = (q-p).cross_product(r) / r.cross_product(s)

        if 0<=t and t<=1 and 0<=u and u<=1:
            poi = p + r.scale(t)
            return poi

        else: return None

def LineSegmentIntersection(S,n):

    P = []
    for i in range(n):
        for j in range(n):

            if j==i: continue
            pt = PairIntersection(S[i],S[j])
            if pt is None: continue
            P.append(pt)

    return P


def main():

    n = int(input("Enter the number of line segments: "))
    S = []
    way = str(input("Do you want to generate the line segments randomly? y/n: "))

    if way=="y":
        for i in range(n):
            p = Point(random.randint(0,25),random.randint(0,25))
            q = Point(random.randint(0,25),random.randint(0,25))
            seg = LineSegment(p,q)
            S.append(seg)

    elif way=="n":
        instr1 = "Enter the line segments in format:\nx1 y1 x2 y2\nx3 y3 x4 y4\n.. .. .. ..\nxm ym xn yn,\n"
        instr2 = "i.e. one line segment per line, the endpoint coordinates of each segment separated by spaces:"
        print(instr1+instr2)

        for i in range(n):
            seg_coords = str(input()).split(" ")
            seg_coords = [float(x) for x in seg_coords]
            p = Point(seg_coords[0],seg_coords[1])
            q = Point(seg_coords[2],seg_coords[3])
            seg = LineSegment(p,q)
            S.append(seg)

    else:
        print("Invalid input! Please try again.")

    P = LineSegmentIntersection(S,n)
    plot_intersegments(S,P)

    for point in P:
        print(point,end=" ")
    print("",end="\n")

if __name__=="__main__":
	main()
