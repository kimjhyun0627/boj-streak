# https://www.acmicpc.net/problem/1197

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline


def find(x):
    if connected[x] != x:
        connected[x] = find(connected[x])
    return connected[x]


def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a > p_b:
        connected[p_a] = connected[p_b]
    else:
        connected[p_b] = connected[p_a]


def kruskal():
    cnt = 0
    res = 0

    for s, e, w in graph:
        if find(s) != find(e):
            union(s, e)
            res += w
            cnt += 1

        if cnt == V - 1:
            break

    return res


V, E = map(int, input().split())

graph = []
for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))


graph.sort(key=lambda x: x[2])
connected = [ii for ii in range(V + 1)]


print(kruskal())
