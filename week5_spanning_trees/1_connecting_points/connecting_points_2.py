# Uses python3
# Using Prim's algorithm
from collections import defaultdict
import sys
import math
from heapq import *


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def minKey(key, mstSet, V):
    minNum = sys.maxsize

    for v in range(V):
        if key[v] < minNum and mstSet[v] == False:
            minNum = key[v]
            min_index = v

    return min_index


def minimum_distance(x, y):
    V = len(x)
    # Key values used to pick minimum weight edge in cut
    key = [sys.maxsize] * V
    parent = [None] * V  # Array to store constructed MST
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    mstSet = [False] * V

    parent[0] = -1

    maps = {node: f"{x[node]},{y[node]}" for node in range(V)}
    graph = defaultdict(dict)
    for i in range(V):
        for j in range(V):
            distance = euclidean_distance(x[i], y[i], x[j], y[j])
            graph[f"{x[i]},{y[i]}"][f"{x[j]},{y[j]}"] = distance

    for i in range(V):
        u = minKey(key, mstSet, V)
        mstSet[u] = True

        for v in range(V):
            if graph[maps[u]][maps[v]] > 0 and mstSet[v] == False and key[v] > graph[maps[u]][maps[v]]:
                key[v] = graph[maps[u]][maps[v]]
                parent[v] = u

    return sum(key)


if __name__ == '__main__':
    #input = sys.stdin.read
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
