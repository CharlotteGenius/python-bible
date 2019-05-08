#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:10:16 2019

@author: xiangyinyu
"""

import matplotlib.pyplot as plt

m = 6
n = 6
x0 = (1,0)# start node
xn = (4,5)# end node
blocks = [(1,1), (2,0),(1,3), (2,3),(3,3),(5,4)]# block nodes

# ====================================================================

# m*n matrix plate, D is for distance
# -1 means inf distance(unvisited)
# 'X' means a block(can't be visited)
D = [[-1 for a in range(n)] for b in range(m)]
for (k,l) in blocks:
    D[k][l] = 'X'
D[x0[0]][x0[1]] = 0
# while it's start point, the distance is 0

# ====================================================================

def Near(p):
    N = []
    near = [(0,1), (1,0), (0,-1), (-1,0)]
    for (i,j) in near:
        N.append((p[0]+i, p[1]+j))
    return N
# 4 surrounding nodes set near the peak p ============================

parent = {}
pre_layer = [x0]
parent[x0] = None

while D[xn[0]][xn[1]] == -1:
    # not reach the end node yet
    next_layer = []
    for x in pre_layer:
        for xi in Near(x):
            if xi[0] in range(m) and xi[1] in range(n) and D[xi[0]][xi[1]] == -1:
                D[xi[0]][xi[1]] = D[x[0]][x[1]] + 1
                next_layer.append(xi)
                # find all the surrounding nodes of the previous layer nodes,
                # and these nodes form the next layer
                parent[xi] = x
                # parent implies the previous node
    pre_layer = next_layer
    # next level became a previous level

# ====================================================================
# till now, we found all the distances in the matrix
# and now, we want to output the route from start to end
# and parent list helps!

# find the route points and plot them out
fig = plt.figure()
ax = fig.add_subplot(111)
'''
fig.add_subplot(221)   #top left
fig.add_subplot(222)   #top right
fig.add_subplot(223)   #bottom left
fig.add_subplot(224)   #bottom right 
'''
ax.set_ylim(m,-1)
ax.set_xlim(-1,n)

for b in blocks:
    plt.plot(b[1],b[0], 'x', color = 'red')
    # red 'X' mark the blocks

end = xn
while end != x0:
    print(end)
    ax.annotate(D[end[0]][end[1]], (end[1], end[0]))
    plt.plot([parent[end][1], end[1]], [parent[end][0], end[0]], marker = 'o', color = 'blue')
    end = parent[end]

plt.show()

