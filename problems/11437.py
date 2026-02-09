# https://www.acmicpc.net/problem/11437

from sys import stdin, setrecursionlimit

setrecursionlimit(10**5)
input = stdin.readline


def dfs(node, d):
    for next in graph[node]:
        if tree[next] == []:
            tree[next] = [node, d + 1]
            dfs(next, d + 1)


def lca(a, b):
    while tree[a][1] != tree[b][1]:
        if tree[a][1] > tree[b][1]:
            a = tree[a][0]
        else:
            b = tree[b][0]
    while a != b:
        a = tree[a][0]
        b = tree[b][0]
    return a


N = int(input())

graph = [[] for _ in range(N + 1)]
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree[1] = [0, 0]
dfs(1, 0)

# print(tree)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))
