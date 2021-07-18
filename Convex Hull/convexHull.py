import sys
import random
from point import *

def SlowConvexHull(P):

    E = list()
    n = len(P)

    for i in range(0,n):
        for j in range(0,n):

            if i==j:
                continue

            p = P[i]
            q = P[j]
            valid = True
            pq = DirectedEdge(p,q)

            for k in range(0,n):

                if k==i or k==j:
                    continue
                r = P[k]
                check = pq.right_turns_with(r)
                if( not check):
                    valid = False
                    break

            if valid:
                E.append(pq)

    L = clockwise_verts(E)
    plot_polygon(P,L,"SlowConvexHull")
    return L

def GrahamsScan(P):

    P.sort(key=lambda lm: (lm.x,lm.y))

    n = len(P)
    L_upp = [P[0],P[1]]

    for i in range(2,n):
        L_upp.append(P[i])
        while (len(L_upp)>2) and (not DirectedEdge(L_upp[-3],L_upp[-2]).right_turns_with(L_upp[-1])):
            del L_upp[-2]

    L_low = [P[n-1],P[n-2]]

    for i in reversed(range(n-2)):
        L_low.append(P[i])
        while (len(L_low)>2) and (not DirectedEdge(L_low[-3],L_low[-2]).right_turns_with(L_low[-1])):
            del L_low[-2]

    del L_low[-1]
    del L_low[0]

    L = L_upp
    L.extend(L_low)
    plot_polygon(P,L,"GrahamsScan")
    return L


def main():

    P = []

    dec = str(input("Do you want the points to be generated randomly? y/n: "))

    if dec=="y":
        n = int(input("Enter the number of points to be generated: "))
        for i in range(n):
            pt = Point(random.randint(0,25),random.randint(0,25))
            P.append(pt)

    elif dec=="n":
        in_str = str(input("Enter the points in format: x1 y1 x2 y2 ... xn yn, i.e. separated by spaces:\n"))
        in_list = in_str.split(" ")

        n = len(in_list)
        for i in range (0,int(n/2)):
            P.append(Point(float(in_list[2*i]), float(in_list[(2*i)+1])))

    else:
        print("Invalid input! Please try again.")
        quit()

    alg = int(sys.argv[1])
    if alg==1:
        L = SlowConvexHull(P)
    elif alg==2:
        L = GrahamsScan(P)
    else:
        print("Error! Wrong command line argument entered")
        quit(1)

    l = len(L)

    for i in range(0,l):
        print(L[i],end="=>")
    print(L[0],end="\n")


if __name__=="__main__":
	main()
