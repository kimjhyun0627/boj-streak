# https://www.acmicpc.net/problem/1967

from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)


def dfs(node: int, visited: list) -> tuple:
    visited[node] = True
    max_distance = 0
    max_node = node

    for next_node, distance in graph[node]:
        if not visited[next_node]:
            next_leaf, max_dist = dfs(next_node, visited)
            
            next_distance = max_dist + distance
            if max_distance < next_distance:
                max_distance = next_distance
                max_node = next_leaf
                
    return max_node, max_distance


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_leaf, _ = dfs(1, [False] * (n + 1))
_, res = dfs(max_leaf, [False] * (n + 1))

print(res)
