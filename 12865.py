# https://www.acmicpc.net/problem/12865

from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
objs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for ii in range(1, N + 1):
    for jj in range(1, K + 1):
        w, v = objs[ii - 1]
        if jj < w:
            dp[ii][jj] = dp[ii - 1][jj]
        else:
            dp[ii][jj] = max(dp[ii - 1][jj], dp[ii - 1][jj - w] + v)

print(max(dp[-1]))
