# Uses python3

import sys
from heapq import *


def djikstra(adj, cost, s, t):
    # write your code here
    heap = []
    distances = [10**10] * len(adj)
    distances[s] = 0

    heappush(heap, (0, s))

    while heap:
        _cost, u = heappop(heap)
        for ind, v in enumerate(adj[u]):
            if distances[v] > distances[u] + cost[u][ind]:
                distances[v] = distances[u] + cost[u][ind]
                heappush(heap, (distances[v], v))

    if distances[t] == 10**10:
        return -1
    return distances[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(djikstra(adj, cost, s, t))
