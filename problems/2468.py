# https://www.acmicpc.net/problem/2468

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]


def dfs(x, y, level):
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    visited[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] > level and not visited[nx][ny]:
            dfs(nx, ny, level)


res = 0

for level in range(101):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for ii in range(n):
        for jj in range(n):
            if graph[ii][jj] > level and not visited[ii][jj]:
                count += 1
                dfs(ii, jj, level)

    res = max(res, count)

print(res)
