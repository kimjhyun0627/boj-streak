# https://www.acmicpc.net/problem/14502

from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
walls = []
virus = []

res = 0
for ii in range(n):
    for jj in range(m):
        if graph[ii][jj] == 0:
            walls.append([ii, jj])
        if graph[ii][jj] == 2:
            virus.append([ii, jj])

for ii in range(len(walls)):
    for jj in range(ii + 1, len(walls)):
        for kk in range(jj + 1, len(walls)):
            cnt = 0
            visited = [
                [True if graph[x][y] else False for y in range(m)] for x in range(n)
            ]
            visited[walls[ii][0]][walls[ii][1]] = True
            visited[walls[jj][0]][walls[jj][1]] = True
            visited[walls[kk][0]][walls[kk][1]] = True

            for v in virus:
                queue = deque()
                queue.append((v[0], v[1]))

                while queue:
                    x, y = queue.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

            for x in range(n):
                for y in range(m):
                    if not visited[x][y]:
                        cnt += 1

            res = max(res, cnt)

print(res)
