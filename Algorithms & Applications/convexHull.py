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
                check = pq.is_r_left_of_pq(r)
                if(check):
                    valid = False
                    break

            if valid:
                E.append(pq)

    L = clockwise_verts(E)
    plot_polygon(P,L,"SlowConvexHull")
    return L


def main():

    P = []
    in_str = str(input("Enter the points in format: x1 y1 x2 y2 ... xn yn, i.e. separated by spaces:\n"))
    in_list = in_str.split(" ")

    n = len(in_list)
    for i in range (0,int(n/2)):
        P.append(Point(float(in_list[2*i]), float(in_list[(2*i)+1])))

    L = SlowConvexHull(P)
    l = len(L)

    for vertex in L:
        print(vertex,end="=>")
    print("\n")


if __name__=="__main__":
	main()
