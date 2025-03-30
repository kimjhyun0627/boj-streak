# https://www.acmicpc.net/problem/2583

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs(x, y) -> int:
    graph[x][y] = -1
    cnt = 1
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if not graph[nx][ny]:
            cnt += dfs(nx, ny)

    return cnt


M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    sx, sy, ex, ey = map(int, input().split())
    for ii in range(sy, ey):
        for jj in range(sx, ex):
            graph[ii][jj] += 1

count = 0
res = []
for ii in range(M):
    for jj in range(N):
        if not graph[ii][jj]:
            count += 1
            res.append(dfs(ii, jj))

print(count)
print(*sorted(res))
