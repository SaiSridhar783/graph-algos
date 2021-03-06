# Uses python3

import sys
from collections import deque


def bipartite(adj):
    # write your code here
    V = len(adj)
    col = [-1]*(V)
    q = deque()

    for i in range(V):
        if (col[i] == -1):
            q.append([i, 0])
            col[i] = 0

            while len(q):
                p = q.popleft()

                # current vertex
                v = p[0]
                # colour of current vertex
                c = p[1]

                for j in adj[v]:
                    if (col[j] == c):
                        return 0

                    if (col[j] == -1):
                        col[j] = int(not c)
                        q.append([j, col[j]])

    return 1


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
    print(bipartite(adj))
