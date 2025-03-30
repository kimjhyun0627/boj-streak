# https://www.acmicpc.net/problem/2252

from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())

degree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    taller, shorter = map(int, input().split())
    degree[shorter] += 1
    graph[taller].append(shorter)

res = []
queue = deque()

for ii in range(1, N + 1):
    if degree[ii] == 0:
        queue.append(ii)

while queue:
    node = queue.popleft()
    res.append(node)

    for g in graph[node]:
        degree[g] -= 1
        if degree[g] == 0:
            queue.append(g)

print(*res)
