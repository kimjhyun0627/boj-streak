# https://www.acmicpc.net/problem/7562

from sys import stdin
from collections import deque

input = stdin.readline

dirs = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

t = int(input())

for _ in range(t):

    l = int(input())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())

    graph = [[10**6 for _ in range(l)] for _ in range(l)]
    graph[sx][sy] = 0

    queue = deque()
    queue.append([sx, sy])

    while queue:
        x, y = queue.popleft()
        if x == tx and y == ty:
            break
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] > graph[x][y] + 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    print(graph[tx][ty])
