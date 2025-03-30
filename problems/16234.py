# https://www.acmicpc.net/problem/16234

from sys import stdin
from collections import deque

input = stdin.readline
DIRS = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def bfs(x, y, cnt):

    visited[x][y] = cnt

    queue = deque([(x, y)])
    s, c = 0, 0
    while queue:
        cx, cy = queue.popleft()
        s += graph[cx][cy]
        c += 1
        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == cnt:
                continue
            if L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
                visited[nx][ny] = cnt
                queue.append((nx, ny))

    return s // c


N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

res = 0
while res <= 2000:
    cnt = 1
    unions = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for ii in range(N):
        for jj in range(N):
            if not visited[ii][jj]:
                avr = bfs(ii, jj, cnt)
                if avr:
                    unions.append((cnt, avr))
                cnt += 1

    if len(unions) == N**2:
        break

    for c, avr in unions:
        for ii in range(N):
            for jj in range(N):
                if visited[ii][jj] == c:
                    graph[ii][jj] = avr

    res += 1

print(res)
