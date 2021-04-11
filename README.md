# Computational Geometry

This repository documents my work done in the Computational Geometry project offered by [WnCC](https://wncc-iitb.org) under Seasons of Code 2021. An overview of the project can be found [here](https://wncc-iitb.org/soc_projects/88-comp-geo.html).

After understanding and implementing some of the fundamental computational geometry algorithms and techniques, I aim to explore the applications of these algorithms in the field of computer graphics as described in [this](http://dpd.cs.princeton.edu/Papers/DobkinIEEE.pdf) article.

## Progress till first checkpoint (11/04/2021)

The following fundamental problems and algorithms to solve them have been studied, and work on implementing them in code, keeping in mind the relevant data structures, has been started.

1. Fixed-Radius Near Neighbour Problem

Given a set _P_ of points in a plane (though one can consider higher dimensional spaces as well) and a distance _r_ > 0, the goal is to find all distinct pairs of points _p_,_q_ such that the Euclidean distance between them is at most _r_. The proposed algorithm starts with the case of 1-dimensional points. Since it uses bucketing, the method is easily generalised to _d_-dimensional points.

2. Convex Hull Problem

Given a set _P_ of points in a plane, output a representation of _P_'s convex hull, i.e. the smallest convex set (polygon) that contains all the points. A simple algorithm of complexity O(n^3) is discussed, where n is the number of points, followed by the more efficient Graham's scan which runs in O(nlogn) time. Another approach is the QuickHull algorithm, which is a somewhat generalized version of the quick-sort procedure. Other algorithms developed to solve this problem include Gift-Wrapping and Jarvis’s March, Output Sensitive Convex Hull Algorithms, and Chan’s Algorithm.

3. Line Segment Intersection

As the name suggests, this problem involves computing intersections. Algorithms to solve this for 2 and 3 dimensional lines find use in many application areas - in computer graphics, the computationally most intensive part of ray shooting is determining the intersection of the ray with other objects in the rendered scene. The basic algorithm is covered, along with the well-known Plane Sweeep algorithm.

4. Polygon Triangulation

Given a polygon _P_, the aim is to decompose it into a set of disjoint triangles. Though an O(n) algorithm has been found, it is too intricate to be used in practical applications. An O(nlogn) algorithm is discussed - it first considers the special case of triangulating a monotone polygon, and then considers how to convert an arbitrary polygon into a collection of disjoint monotone polygons such that the first part of the algorithm can be applied to them.

## Primary Resources

* Computational Geometry: Algorithms and Applications. [Link](https://people.inf.elte.hu/fekete/algoritmusok_msc/terinfo_geom/konyvek/Computational%20Geometry%20-%20Algorithms%20and%20Applications,%203rd%20Ed.pdf)

* CMSC 754 lecture notes by Prof. David M. Mount, University of Maryland. [Link](https://www.cs.umd.edu/~mount/754/Lects/754lects.pdf)

* Computational Geometry - online course on Coursera. [Link](https://www.coursera.org/learn/computational-geometry)
