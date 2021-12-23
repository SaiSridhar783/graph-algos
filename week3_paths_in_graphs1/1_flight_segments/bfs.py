# Uses python3

import sys
from collections import deque


def distance(adj, s, t):
    # write your code here
    q = deque([s])
    visited = [False] * len(adj)
    #count = [-1] * len(adj)
    dist = 0
    while q:
        l = len(q)
        for _ in range(l):
            node = q.popleft()
            visited[node] = True
            #count[node] = dist
            if node == t:
                return dist

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour] = True

        dist += 1

    # return count[t]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
