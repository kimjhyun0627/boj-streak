# https://www.acmicpc.net/problem/1507

from sys import stdin

input = stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
remove = [[(False if graph[ii][jj] != 0 else True) for jj in range(N)] for ii in range(N)]

for ii in range(N):
    for jj in range(N):
        for kk in range(N):
            if ii == jj or ii == kk or jj == kk:
                continue
            if graph[ii][jj] == graph[ii][kk] + graph[kk][jj]:
                remove[ii][jj] = True
            elif graph[ii][jj] > graph[ii][kk] + graph[kk][jj]:
                print(-1)
                exit(0)

ans = 0
for ii in range(N):
    for jj in range(ii, N):
        if not remove[ii][jj]:
            ans += graph[ii][jj]

print(ans)
