## Line Segment Intersection Problem

Running instructions:

<code> python3 lineSegIntersect.py </code>

After running the above instruction, the program will ask for

1. the number of line segments in the set
2. whether you want to generate the segments randomly (y) or not (n)
3. If the answer to the previous question is no, then the program will ask for input of the coordinates of the endpoints of the line segments in the following format:
One line segment per line, each segment in the format <code>x1 y1 x2 y2</code>, i.e. the coordinates separated by spaces, where (x1, y1) is one endpoint of the segment and (x2, y2) is the other.

Example input of the line segments' coordinate data: 

<code>8 6 2 9</code> <br>
<code>8 7 5 3</code> <br>
<code>4 6 5 1</code> <br>
<code>0 9 6 9</code> <br>
<code>4 7 5 6</code> <br>
<code>5 2 9 8</code> <br>
<code>1 3 8 0</code> <br>

A png file with the entered/randomly generated line segments drawn in blue and the computed points of intersection marked in red will be produced, and the points of intersection will be printed as output.

Example 1                  |  Example 2
:-------------------------:|:-------------------------:
![](LinSegInt_0.png)  |  ![](LinSegInt_1.png)
