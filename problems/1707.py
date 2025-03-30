# https://www.acmicpc.net/problem/1707

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


def dfs(start, visited, graph, group):
    visited[start] = group

    for v in graph[start]:
        if visited[v] == 0:
            result = dfs(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    for _ in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    for ii in range(1, V + 1):
        if visited[ii] == 0:
            result = dfs(ii, visited, graph, 1)

            if not result:
                break

    print("YES") if result else print("NO")
