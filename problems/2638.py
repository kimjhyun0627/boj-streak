# https://www.acmicpc.net/problem/2638

from sys import stdin, setrecursionlimit

input = lambda: stdin.readline().rstrip()
setrecursionlimit(10**6)

dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def check():
    for pa in paper:
        for p in pa:
            if p == 1:
                return True
    return False


def melt():
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if paper[x][y] == 1:
                count = 0
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if paper[nx][ny] == 2:
                        count += 1
                if count >= 2:
                    paper[x][y] = 0


def update(x, y):
    visited[x][y] = True
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if paper[nx][ny] == 0 or paper[nx][ny] == 2:
                paper[nx][ny] = 2
                update(nx, ny)


N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

update(0, 0)
res = 0
while check():
    melt()
    res += 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    update(0, 0)

print(res)
