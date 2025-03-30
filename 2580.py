# https://www.acmicpc.net/problem/2580

from sys import stdin

input = stdin.readline
SIZE = 9


def candidate(x, y):
    xarea, yarea = x // 3 * 3, y // 3 * 3
    area = set(range(1, 10))
    for ii in range(xarea, xarea + 3):
        for jj in range(yarea, yarea + 3):
            if sdoku[ii][jj]:
                area.discard(sdoku[ii][jj])

    col = set(range(1, 10))
    row = set(range(1, 10))
    for ii in range(SIZE):
        if sdoku[x][ii]:
            col.discard(sdoku[x][ii])
        if sdoku[ii][y]:
            row.discard(sdoku[ii][y])

    return area & row & col


def dfs(idx):

    if idx == len(empty):
        for s in sdoku:
            print(*s)
        exit(0)

    x, y = empty[idx]
    for c in candidate(x, y):
        sdoku[x][y] = c
        dfs(idx + 1)
        sdoku[x][y] = 0


sdoku = [list(map(int, input().split())) for _ in range(SIZE)]
empty = [(ii, jj) for ii in range(SIZE) for jj in range(SIZE) if sdoku[ii][jj] == 0]

dfs(0)
