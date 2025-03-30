# https://www.acmicpc.net/problem/2644

from sys import stdin

input = stdin.readline


def dfs(v, count):
    visited[v] = True
    if v == B:
        return count

    res = []
    for g in graph[v]:
        if not visited[g]:
            res.append(dfs(g, count + 1))

    res = [r for r in res if r >= 0]
    return min(res) if res else -1


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

A, B = map(int, input().split())

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(dfs(A, 0))
