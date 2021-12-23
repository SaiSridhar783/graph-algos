# Uses python3
# Using Kruskal's algorithm
import sys
import math
from heapq import *


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# A utility function to find set of an element i
# (uses path compression technique)


def find(parent, i, maps):
    if parent[maps[i]] == i:
        return i
    return find(parent, parent[maps[i]], maps)

# A function that does union of two sets of x and y
# (uses union by rank)


def union(parent, rank, x, y, maps):
    xroot = find(parent, x, maps)
    yroot = find(parent, y, maps)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[maps[xroot]] < rank[maps[yroot]]:
        parent[maps[xroot]] = yroot
    elif rank[maps[xroot]] > rank[maps[yroot]]:
        parent[maps[yroot]] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[maps[yroot]] = xroot
        rank[maps[xroot]] += 1


def minimum_distance(x, y):
    result = 0
    # write your code here
    V = len(x)
    heap = []
    for i in range(V):
        for j in range(i+1, V):
            distance = euclidean_distance(x[i], y[i], x[j], y[j])
            heappush(heap, (distance, f"{x[i]},{y[i]}", f"{x[j]},{y[j]}"))

    parent = []
    rank = []

    maps = {f"{x[node]},{y[node]}": node for node in range(V)}

    for node in range(V):
        parent.append(f"{x[node]},{y[node]}")
        rank.append(0)

    e = 0
    while e < V-1:
        w, u, v = heappop(heap)
        x = find(parent, u, maps)
        y = find(parent, v, maps)

        if x != y:
            e += 1
            result += w
            union(parent, rank, x, y, maps)

    return result


if __name__ == '__main__':
    #input = sys.stdin.read
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
