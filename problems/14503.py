# https://www.acmicpc.net/problem/14503

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * M for _ in range(N)]
visited[r][c] = 1
cleaned = 1

while True:
    found = False

    for _ in range(4):
        d = (d + 3) % 4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                r, c = nx, ny
                cleaned += 1
                found = True
                break

    if not found:
        back_dir = (d + 2) % 4
        bx = r + dx[back_dir]
        by = c + dy[back_dir]

        if 0 <= bx < N and 0 <= by < M and graph[bx][by] == 0:
            r, c = bx, by
        else:
            break

print(cleaned)
