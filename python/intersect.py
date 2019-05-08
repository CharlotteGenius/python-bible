#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:32:51 2018

@author: xiangyinyu
"""
#!/usr/bin/python

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
    if (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x):
        return True

def intersect(A,B,C,D):
    if ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D):
        return True


a = Point(0,0)
b = Point(0,1)
c = Point(1,1)
d = Point(1,0)


print (intersect(a,b,c,d))
print (intersect(a,c,b,d))
print (intersect(a,d,b,c))