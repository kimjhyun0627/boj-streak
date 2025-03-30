# https://www.acmicpc.net/problem/15686

from sys import stdin
from itertools import combinations

input = stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicken = []
for ii in range(N):
    for jj in range(N):
        if graph[ii][jj] == 2:
            chicken.append((ii, jj))

selections = combinations(chicken, M)

res = float("inf")
for select in selections:
    new_graph = [[1 if graph[ii][jj] == 1 else 0 for jj in range(N)] for ii in range(N)]
    for s in select:
        new_graph[s[0]][s[1]] = 2

    dist = 0
    for ii in range(N):
        for jj in range(N):
            if new_graph[ii][jj] == 1:
                dist += min([abs(s[0] - ii) + abs(s[1] - jj) for s in select])

    res = min(res, dist)

print(res)
