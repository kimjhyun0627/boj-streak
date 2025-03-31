# https://www.acmicpc.net/problem/17070

from sys import stdin
from enum import Enum

input = lambda: stdin.readline().rstrip()


class state(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    CROSS = 2


def dfs(position):
    global cnt
    x, y, dir = position
    if x == N - 1 and y == N - 1:
        cnt += 1
        return

    if x + 1 < N and y + 1 < N:
        if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs((x + 1, y + 1, state.CROSS))

    if dir == state.HORIZONTAL or dir == state.CROSS:
        if y + 1 < N:
            if graph[x][y + 1] == 0:
                dfs((x, y + 1, state.HORIZONTAL))

    if dir == state.VERTICAL or dir == state.CROSS:
        if x + 1 < N:
            if graph[x + 1][y] == 0:
                dfs((x + 1, y, state.VERTICAL))


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
dfs((0, 1, state.HORIZONTAL))

print(cnt)
