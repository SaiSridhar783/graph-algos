# Uses python3

import sys
from collections import deque


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    V = len(adj)
    distance[s] = 0
    reachable[s] = 1
    negative_nodes = deque()

    for _ in range(V-1):
        for u in range(V):
            for i, v in enumerate(adj[u]):
                if distance[u] + cost[u][i] < distance[v]:
                    distance[v] = distance[u] + cost[u][i]
                    reachable[v] = 1

    for u in range(V):
        for i, v in enumerate(adj[u]):
            if distance[u] + cost[u][i] < distance[v]:
                negative_nodes.append(v)

    visited = [0] * V
    while negative_nodes:
        u = negative_nodes.popleft()
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v]:
                negative_nodes.append(v)


if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [float("inf")] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
