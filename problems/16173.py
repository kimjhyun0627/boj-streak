# https://www.acmicpc.net/problem/16173

from sys import stdin

input = stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]


def dfs(x, y):
    if x == N - 1 and y == N - 1:
        return True
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if visited[x][y]:
        return False
    visited[x][y] = True
    return dfs(x + board[x][y], y) or dfs(x, y + board[x][y])


print("HaruHaru" if dfs(0, 0) else "Hing")
