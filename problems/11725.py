# https://www.acmicpc.net/problem/11725

from sys import stdin

input = stdin.readline


def dfs(graph, node):

    stack = [node]
    while stack:
        top = stack.pop()
        for adj in graph[top]:
            if visited[adj] == 0:
                visited[adj] = top
                stack.append(adj)

    return visited


n = int(input())

graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    e, f = map(int, input().split())
    graph[e].append(f)
    graph[f].append(e)

visited = [0] * (n + 1)

dfs(graph, 1)

for x in range(2, n + 1):
    print(visited[x])
