# https://www.acmicpc.net/problem/1717

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

    if x != y:
        if x < y:
            sets[y] = x
        else:
            sets[x] = y


N, M = map(int, input().split())
sets = [ii for ii in range(N + 1)]

for _ in range(M):
    order, a, b = map(int, input().split())
    if order:
        print("YES" if find(a) == find(b) else "NO")

    else:
        union(a, b)

    print(sets)
