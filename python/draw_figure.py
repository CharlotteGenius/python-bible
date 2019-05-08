#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 16:52:08 2018

@author: xiangyinyu
"""

import numpy as np
import matplotlib.pyplot as plt

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

A = Point(5,12)
B = Point(2,10)
C = Point(8,6)
D = Point(4,2)
E = Point(6,3)

points = [A, B, C, D, E]
l = len(points)

# counterclockwise order:
# If the slope of the line AB is 
# less than the slope of the line AC 
# then the three points are listed in a counterclockwise order
def ccw(A,B,C):
    if (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x):
        return True

# These intersect if and only if points A and B are separated
# by segment CD and points C and D are separated by segment AB
# ACD and BCD should have opposite orientation 
# meaning either ACD or BCD is counterclockwise but not both
def intersect(A,B,C,D):
    if ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D):
        return True

for a in range(0, l): 
    for b in range(a+1,l):
        for c in range(b,l):
            for d in range(c+1,l):
                point1 = points[a]
                point2 = points[b]
                l1_x_min = min(point1.x, point2.x)
                l1_x_max = max(point1.x, point2.x)
                l1_y_min = min(point1.y, point2.y)
                l1_y_max = max(point1.y, point2.y)
                point3 = points[c]
                point4 = points[d]
                l2_x_min = min(point3.x, point4.x)
                l2_x_max = max(point3.x, point4.x)
                l2_y_min = min(point3.y, point4.y)
                l2_y_max = max(point3.y, point4.y)
                plt.plot([point1.x, point2.x],  [point1.y, point2.y], marker = 'o')
                plt.plot([point3.x, point4.x],  [point3.y, point4.y], marker = 'o')

#for lines in plt.plot():
#    if intersect(*points):
#        plt.del()

plt.show()









