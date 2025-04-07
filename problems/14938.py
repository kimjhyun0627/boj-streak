# https://www.acmicpc.net/problem/14938

import heapq
from sys import stdin

input = lambda: stdin.readline().rstrip()

INF = 10**9
N, M, R = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    D[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if D[now] < dist:
            continue

        for g in graph[now]:
            cost = dist + g[1]
            if cost < D[g[0]]:
                D[g[0]] = cost
                heapq.heappush(queue, (cost, g[0]))


res = 0
for ii in range(1, N + 1):
    D = [INF for _ in range(N + 1)]
    dijkstra(ii)

    cnt = 0
    for d in range(1, N + 1):
        if M >= D[d]:
            cnt += items[d]

    res = max(res, cnt)

print(res)
