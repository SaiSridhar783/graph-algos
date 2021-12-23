# Uses python3
# Using Kruskal's algorithm
import sys
import math
from heapq import *


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# A utility function to find set of an element i
# (uses path compression technique)


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# A function that does union of two sets of x and y
# (uses union by rank)


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1




def minimum_distance(x, y):
    result = 0
    # write your code here
    heap = []
    V = len(x)

    for i in range(V):
        for j in range(i+1, V):
            distance = euclidean_distance(x[i], y[i], x[j], y[j])
            heappush(heap, (distance, f"{x[i]},{y[i]}", f"{x[j]},{y[j]}"))

    visited = [set([f"{x[i]},{y[i]}"]) for i in range(V)]
    ans = []
    c = 0
    while heap:
        if c == V-1:
            break
        distance, point1, point2 = heappop(heap)
        for disjoint in visited:
            if point1 in disjoint and point2 in disjoint:
                break

        else:
            for i in visited:
                if point1 in i:
                    i.add(point2)
                elif point2 in i:
                    i.add(point1)

            result += distance

            ans.append((distance, point1, point2))
            c += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
