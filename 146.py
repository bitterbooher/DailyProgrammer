"""
A Polygon[2] is a geometric two-dimensional figure that has n-sides (line segments) that closes to form a loop. 
Polygons can be in many different shapes and have many different neat properties, though this challenge is about Regular Polygons[3] . 
Our goal is to compute the permitter of an n-sided polygon that has equal-length sides given the circumradius[4] . 
This is the distance between the center of the Polygon to any of its vertices; not to be confused with the apothem[5] 

"""
from math import sin, pi
# where nos is the number of sides of the polygon, from 3 to n
# where circradius ranges from .01 to 100 inclusive 
# circumradius is the distance from the centre to any of the vertices of the poylgon


def polygonperim(nos, circradius):
	print 2*nos*circradius*sin(pi/nos)
	
polygonperim(5, 3.7)



