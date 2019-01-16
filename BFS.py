#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 22:32:10 2019

@author: xiangyinyu
"""
# BFS Breadth-First-Search 广度优先搜索
# 是一层一层的取点

# 每个点的连接点
Graph = {
        'A':['B','C'],
        'B':['A','C','D'],
        'C':['A','B','D','E'],
        'D':['B','C','E','F'],
        'E':['C','D'],
        'F':['D'],
        }

def BFS(graph, s):
    queue = []
    # 队列，先进先出
    seen = []
    # 已经跑过的点
    parent = {}
    # 因为BFS是分层的，比如从A出发，B在第二次，那么A到B的最短路径为1
    # parent用于记录每一个点的前一个点，便于用于找到最短路径
    
    queue.append(s)
    seen.append(s)
    parent[s] = None
    # 起始点没有前一个点
    
    while len(queue)>0:
        vertex = queue.pop(0)
        # 总是取第一个点，并将此点从队列里拿出
        nodes = graph[vertex]
        
        for n in nodes:
            if n not in seen:
                queue.append(n)
                seen.append(n)
                # 那么n的上层肯定是vertex
                parent[n] = vertex
    return parent
    # 一直拿出第一个，知道队列里没有点可拿出
    
start = 'A'
Parent = BFS(Graph,start)

# 如果设置终点，需要找两个点的最短路径
end = 'F'
way = []
while end != None:
    way.append(end)
    end = Parent[end]
    # 从终点找每个点的前一个点，一直到起点
for w in way[::-1]:
    print(w)