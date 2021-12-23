# Uses python3

import sys

sys.setrecursionlimit(200000)


def DFS(adj, used, v):
    used[v] = 1
    for neighbour in adj[v]:
        if not used[neighbour]:
            DFS(adj, used, neighbour)


def dfs_post(adj, used, v, post, count):
    # write your code here
    used[v] = 1
    for neighbour in adj[v]:
        if not used[neighbour]:
            dfs_post(adj, used, neighbour, post, count)

    count[0] += 1
    post[v] = count[0]


def number_of_strongly_connected_components(adj, adj_rev):
    used = [0] * len(adj)
    post = [0] * len(adj)
    check = [0]
    for v in range(len(adj)):
        if not used[v]:
            dfs_post(adj_rev, used, v, post, check)

    result = 0
    used = [0] * len(adj)
    for _ in range(len(adj)):
        x = post.index(max(post))
        post[x] = -1
        if not used[x]:
            result += 1
            DFS(adj, used, x)

    # write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read
    data = list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_rev = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_rev[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, adj_rev))
