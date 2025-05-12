# https://www.acmicpc.net/problem/1647

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = lambda: stdin.readline().rstrip()


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx != ry:
        parent[ry] = rx


N, M = map(int, input().split())
edges = []
for _ in range(M):
    fr, to, cost = map(int, input().split())
    edges.append((cost, fr, to))

edges.sort()

parent = [ii for ii in range(N + 1)]
total = 0
last = 0

for cost, fr, to in edges:
    if find(fr) != find(to):
        union(fr, to)
        total += cost
        last = cost

print(total - last)
