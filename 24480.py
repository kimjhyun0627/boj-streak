# https://www.acmicpc.net/problem/24480

from sys import stdin, setrecursionlimit
from collections import defaultdict

setrecursionlimit(10**6)
input = lambda: stdin.readline().rstrip()


def dfs(r):
    global idx
    visited[r] = idx

    for g in graph[r]:
        if not visited[g]:
            idx += 1
            dfs(g)


N, M, R = map(int, input().split())
graph = defaultdict(list)
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for k, v in graph.items():
    v.sort(reverse=True)

idx = 1
dfs(R)
for v in visited[1:]:
    print(v)
