# Uses python3

import sys


def DFS(adj, visited, curStack, x, ans):
    visited[x] = True
    curStack[x] = True

    for y in adj[x]:
        if not visited[y]:
            DFS(adj, visited, curStack, y, ans)
        else:
            if curStack[y]:
                ans[0] = 1
                return

    curStack[x] = False


def acyclic(adj):
    visited = [False] * len(adj)
    curStack = [False] * len(adj)
    ans = [0]
    for x in range(len(adj)):
        if not visited[x]:
            DFS(adj, visited, curStack, x, ans)

        if ans[0] == 1:
            return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
