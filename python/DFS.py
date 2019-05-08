#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:49:34 2019

@author: xiangyinyu
"""

# DFS Depth-First-Search 深度优选搜索
# 是一条路走到黑，再返回终点前的一个点，找其他未走过的点
Graph = {
        'A':['B','C'],
        'B':['A','C','D'],
        'C':['A','B','D','E'],
        'D':['B','C','E','F'],
        'E':['C','D'],
        'F':['D'],
        }

def DFS(graph, s):
    stack = []
    seen = []
    parent = {}
    # 运用栈，后进先出
    stack.append(s)
    seen.append(s)
    parent[s] = None
    
    while len(stack)>0:
        vertex = stack.pop(-1)
        nodes = Graph[vertex]
        for n in nodes[::-1]:
            # 因为是先进后出，所以先放入的点沉底了
            # 所以相当于，从后往前取点
            if n not in seen:
                stack.append(n)
                seen.append(n)
                parent[n] = vertex
    return parent
  
start = 'E'
end = 'F'

Parent = DFS(Graph,start)
print(Parent)

# 如果设置终点，需要找两个点的最短路径
way = []
while end != None:
    way.append(end)
    end = Parent[end]
    # 从终点找每个点的前一个点，一直到起点
for w in way[::-1]:
    print(w)
    