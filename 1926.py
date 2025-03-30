# https://www.acmicpc.net/problem/1926

from sys import stdin

input = stdin.readline
DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y):

    visited[x][y] = True
    queue = [(x, y)]
    cnt = 0
    while queue:
        cx, cy = queue.pop(0)
        cnt += 1
        for dx, dy in DIRS:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny]:
                continue
            if paper[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return cnt


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

count, res = 0, 0
for ii in range(N):
    for jj in range(M):
        if paper[ii][jj] and not visited[ii][jj]:
            res = max(res, dfs(ii, jj))
            count += 1

print(count)
print(res)
