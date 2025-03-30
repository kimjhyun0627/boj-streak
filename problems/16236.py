# https://www.acmicpc.net/problem/16236

from sys import stdin
from collections import deque

input = stdin.readline

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(x, y):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque([(x, y)])
    cand = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for dx, dy in dirs:
            ii, jj = i + dx, j + dy

            if 0 <= ii and ii < N and 0 <= jj and jj < N and not visited[ii][jj]:
                if space[x][y] > space[ii][jj] and space[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif space[x][y] == space[ii][jj]:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append((ii, jj))
                elif space[ii][jj] == 0:
                    visited[ii][jj] = visited[i][j] + 1
                    queue.append((ii, jj))

    return sorted(cand, key=lambda x: (x[0], x[1], x[2]))


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
size = [2, 0]
xpos, ypos = -1, -1
for ii in range(N):
    for jj in range(N):
        if space[ii][jj] == 9:
            xpos, ypos = ii, jj
            break

while True:
    space[xpos][ypos] = size[0]
    cand = deque(bfs(xpos, ypos))

    if not cand:
        break

    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[xpos][ypos] = 0
    xpos, ypos = xx, yy

print(cnt)
