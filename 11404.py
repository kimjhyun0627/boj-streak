# https://www.acmicpc.net/problem/11404

from sys import stdin

input = stdin.readline

n = int(input())
m = int(input())
INF = 1e9
cities = [[INF] * (n) for _ in range(n)]

for _ in range(m):
    fr, to, cost = map(int, input().split())
    cities[fr - 1][to - 1] = min(cities[fr - 1][to - 1], cost)

for ii in range(n):
    cities[ii][ii] = 0

for ii in range(n):
    for jj in range(n):
        for kk in range(n):
            cities[jj][kk] = min(cities[jj][kk], cities[jj][ii] + cities[ii][kk])

for ii in range(n):
    for jj in range(n):
        if cities[ii][jj] == INF:
            cities[ii][jj] = 0
            
for c in cities:
    print(*c)
