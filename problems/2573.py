# https://www.acmicpc.net/problem/2573

from sys import stdin, setrecursionlimit

setrecursionlimit(10**4)

input = stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
water = [[0 for _ in range(M)] for _ in range(N)]


def calc_water():
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for ii in range(1, N - 1):
        for jj in range(1, M - 1):
            water[ii][jj] = len(
                [
                    graph[ii + dx][jj + dy]
                    for dx, dy in dirs
                    if graph[ii + dx][jj + dy] == 0
                ]
            )


def melt():
    for ii in range(N):
        for jj in range(M):
            graph[ii][jj] = max(0, graph[ii][jj] - water[ii][jj])


def find():
    first = False
    for ii in range(N):
        for jj in range(M):
            if graph[ii][jj] != 0 and not visited[ii][jj]:
                if first == True:
                    return True
                visited[ii][jj] = True
                dfs(ii, jj)
                first = True
    return False


def dfs(x, y):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


ans = 0
while sum([sum(w) for w in graph]) != 0:
    calc_water()
    melt()
    ans += 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    if find():
        print(ans)
        exit()

print(0)
