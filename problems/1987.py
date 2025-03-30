# https://www.acmicpc.net/problem/1987

from sys import stdin

input = stdin.readline


def bfs(x, y):
    max_len = 1

    q = set([(x, y, graph[y][x])])
    while q:
        x, y, alpha = q.pop()
        max_len = max(max_len, len(alpha))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] not in alpha:
                q.add((nx, ny, alpha + graph[ny][nx]))
    return max_len


r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(0, 0))
