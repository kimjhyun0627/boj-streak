# https://www.acmicpc.net/problem/11779

from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()
INF = 10**9


N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    fr, to, cost = map(int, input().split())
    bus[fr].append((to, cost))

start, end = map(int, input().split())

distances = [INF for _ in range(N + 1)]
distances[start] = 0
parent = [-1 for _ in range(N + 1)]

hqueue = []
heappush(hqueue, (0, start))
while hqueue:
    dist, x = heappop(hqueue)

    if dist > distances[x]:
        continue

    for b in bus[x]:
        ndist = dist + b[1]
        if ndist < distances[b[0]]:
            distances[b[0]] = ndist
            parent[b[0]] = x
            heappush(hqueue, (ndist, b[0]))

cur = end
path = []
while cur != start:
    path.append(cur)
    cur = parent[cur]

path.append(start)
path.reverse()

print(distances[end])
print(len(path))
print(*path)
