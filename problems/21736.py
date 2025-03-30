# https://www.acmicpc.net/problem/21736

from sys import stdin

input = stdin.readline


def bfs(x, y):

    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    queue = [(x, y)]
    meets = 0
    while queue:
        px, py = queue.pop()

        for dx, dy in dir:
            nx, ny = px + dx, py + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            if campus[nx][ny] == "X":
                continue
            if campus[nx][ny] == "P":
                meets += 1
            queue.append((nx, ny))

    return meets


n, m = map(int, input().rstrip().split())
campus = [list(input().rstrip()) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

for ii in range(n):
    for jj in range(m):
        if campus[ii][jj] == "I":
            visited[ii][jj] = True
            res = bfs(ii, jj)
            print(res if res else "TT")
            break
