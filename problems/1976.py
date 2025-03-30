# https://www.acmicpc.net/problem/1976

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


def find(x):
    if x == sets[x]:
        return x
    sets[x] = find(sets[x])
    return sets[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x < y:
        sets[y] = x
    else:
        sets[x] = y


N = int(input())
M = int(input())

maps = [list(map(int, input().split())) for _ in range(N)]
sets = [ii for ii in range(N)]

for ii in range(N):
    for jj in range(N):
        if maps[ii][jj]:
            union(ii, jj)

plan = list(map(int, input().split()))

root = -1
for p in plan:
    if root == -1:
        root = find(p - 1)
        continue
    if root != find(p - 1):
        print("NO")
        exit(0)

print("YES")
