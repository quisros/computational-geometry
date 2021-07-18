from point import *
from aux import *
import matplotlib.pyplot as plt
import math

def VoronoiDiagram(P):

	S = []
	n = len(P)

	(ll, ur) = BoundingBox(P)

	for idx in range(n):

		voronoi_segment_list = []
		# Step 1: find nearest point

		if idx < n-1: jdx_min = idx + 1
		else: jdx_min = idx - 1

		d_min = P[idx].distance(P[jdx_min])

		for jdx in range(n):
			if jdx != idx:
				d = P[idx].distance(P[jdx])
				if d < d_min:
					d_min = d
					jdx_min = jdx

		# Step 2: find all perpendicular lines

		perp_line_list = []

		for jdx in range(n):

			if jdx!=idx:
				midpoint = (P[idx]+P[jdx]).scale(0.5)
				init_slope = (P[jdx].y - P[idx].y) / (P[jdx].x - P[idx].x)
				perp_slope = -1/init_slope
				y_intercept = midpoint.y - (perp_slope*midpoint.x)

				if jdx == jdx_min: first_perp_line_idx = len(perp_line_list)
				perp_line_list.append((perp_slope, y_intercept, midpoint))

		# Step 3: find the first voronoi segment

		midp_nought = (P[idx]+P[jdx_min]).scale(0.5)
		slope_0 = perp_line_list[first_perp_line_idx][0]
		intercept_0 = perp_line_list[first_perp_line_idx][1]

		intersection_list = []

		intersection_list.append((Point(ll.x, (slope_0 * ll.x) + intercept_0), slope_0, intercept_0))
		intersection_list.append((Point(ur.x, (slope_0 * ur.x) + intercept_0), slope_0, intercept_0))

		for line in perp_line_list:

			slope = line[0]
			intercept = line[1]

			if slope != slope_0 and intercept != intercept_0:
				intrsc_x = (intercept - intercept_0) / ( slope_0 - slope )
				intersection_list.append((Point(intrsc_x,(slope * intrsc_x) + intercept),slope,intercept))

		intersection_list.sort(key=lambda l: l[0].x)

		line_0_list = []

		for i in range(len(intersection_list)-1):

			pt_i = intersection_list[i][0]
			pt_i1 = intersection_list[i+1][0]

			if midp_nought.x > pt_i.x and midp_nought.x < pt_i1.x:

				voronoi_segment_list.append((pt_i,pt_i1,slope_0,intercept_0))
				line_0_list.append(intersection_list[i])
				line_0_list.append(intersection_list[i+1])

		# Step 4: find all voronoi segments

		while line_0_list:

			new_line_0_list = []
			new_voronoi_segment_list = []

			for line_0 in line_0_list:

				pt_0 = line_0[0]
				slope_0 = line_0[1]
				intercept_0 = line_0[2]

				intersection_list = []

				fx_min = slope_0 * ll.x + intercept_0
				d = Point(ll.x, fx_min).distance(pt_0)
				intersection_list.append((Point(ll.x, fx_min),d,slope_0,intercept_0))

				fx_min = slope_0 * ur.x + intercept_0
				d = Point(ur.x, fx_min).distance(pt_0)
				intersection_list.append((Point(ur.x, fx_min),d,slope_0,intercept_0))

				for line in perp_line_list:

					slope = line[0]
					intercept = line[1]

					if slope != slope_0 and intercept != intercept_0:

						intersection_x = (intercept - intercept_0) / ( slope_0 - slope )

						fx_min = slope * intersection_x + intercept
						d = Point(intersection_x, fx_min).distance(pt_0)
						intersection_list.append((Point(intersection_x, fx_min),d,slope,intercept))

				intersection_list.sort(key=lambda l: l[0].x)
				intersection_list_filtered = []

				for intersection in intersection_list:

					#if intersection[2] != 0.0:
					if abs(intersection[1]) > 0.000000001:

						for voronoi_segment in voronoi_segment_list:

							a = P[idx].y - ( voronoi_segment[2] * P[idx].x  + voronoi_segment[3] )
							b = intersection[0].y - ( voronoi_segment[2] * intersection[0].x  + voronoi_segment[3] )

							if a > 0.0 and b > 0.0: intersection_list_filtered.append(intersection)
							if a < 0.0 and b < 0.0: intersection_list_filtered.append(intersection)


				intersection_list_filtered.sort(key=lambda x: x[1])

				if len(intersection_list_filtered)>0:

					intersection_slope = intersection_list_filtered[0][2]
					intersection_intercept = intersection_list_filtered[0][3]

					cond = True
					for voronoi_segment in voronoi_segment_list:
						if intersection_slope == voronoi_segment[2] and intersection_intercept == voronoi_segment[3]:
							cond = False

					for new_line_0 in new_line_0_list:
						if intersection_slope == new_line_0[1] and intersection_intercept == new_line_0[2]:
							cond = False

					if cond:
						new_line_0_list.append((
						intersection_list_filtered[0][0],
						intersection_list_filtered[0][2],
						intersection_list_filtered[0][3]))

					new_voronoi_segment_list.append((pt_0,intersection_list_filtered[0][0],slope_0,intercept_0))

			for new_voronoi_segment in new_voronoi_segment_list:
				voronoi_segment_list.append(new_voronoi_segment)

			line_0_list = new_line_0_list

		for voronoi_segment in voronoi_segment_list:
			seg = Segment(voronoi_segment[0],voronoi_segment[1])
			S.append(seg)

	return S



def get_points():

	P = []

	dec = str(input("Do you want the points to be generated randomly? y/n: "))

	if dec=="y":
		n = int(input("Enter the number of points to be generated: "))
		for i in range(n):
			pt = Point(random.uniform(0.0,25.0),random.uniform(0.0,25.0))
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

	return P

def main():

	P = get_points()
	S = VoronoiDiagram(P)
	plot_voronoi(P,S)

if __name__=="__main__":
	main()
