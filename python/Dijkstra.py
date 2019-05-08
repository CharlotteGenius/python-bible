#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:38:06 2019

@author: xiangyinyu
"""

# Dijkstra算法是BFS的延伸
# 在BFS中，每条路径的长度都为1，所以在队列中，直接放入第二层的点
# 即上一个点直接连接的点，我们默认了长度为1
# 而在Dijkstra中，路径的长度不一定为1
# 比如A到B距离为5，而A到C距离为1，那么队列中C应该排在B前面