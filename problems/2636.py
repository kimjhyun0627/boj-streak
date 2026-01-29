# https://www.acmicpc.net/problem/2636

from sys import stdin, setrecursionlimit

setrecursionlimit(10**4)
input = stdin.readline

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]


def check_hole():
    dfs(0, 0, 0)
    for ii in range(1, N - 1):
        for jj in range(1, M - 1):
            if board[ii][jj] != 1 and not visited[ii][jj]:
                dfs(ii, jj, 2)


def dfs(x, y, target):
    visited[x][y] = True
    board[x][y] = target
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 1 and not visited[nx][ny]:
            dfs(nx, ny, target)


def melt():
    for ii in range(1, N - 1):
        for jj in range(1, M - 1):
            if board[ii][jj] == 1:
                if 0 in [board[ii + dx][jj + dy] for dx, dy in dirs]:
                    board[ii][jj] = -1


def cleanup():
    for ii in range(1, N - 1):
        for jj in range(1, M - 1):
            if board[ii][jj] == -1:
                board[ii][jj] = 0


ans = 0
count = sum(b.count(1) for b in board)

while True:
    tmp = sum(b.count(1) for b in board)
    if tmp == 0:
        break
    ans += 1
    count = tmp

    visited = [[False for _ in range(M)] for _ in range(N)]
    check_hole()
    melt()
    cleanup()


print(ans)
print(count)
