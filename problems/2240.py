# https://www.acmicpc.net/problem/2240

from sys import stdin

input = stdin.readline

T, W = map(int, input().split())
drops = [0] + [int(input()) for _ in range(T)]
dp = [[0 for _ in range(W+1)] for _ in range(T+1)]

for ii in range(1, T + 1):
    if drops[ii] == 1:
        dp[ii][0] = dp[ii - 1][0] + 1
    else:
        dp[ii][0] = dp[ii - 1][0]

    for jj in range(1, W + 1):
        if (drops[ii] == 1 and jj % 2 == 0) or (drops[ii] == 2 and jj % 2 != 0):
            dp[ii][jj] = max(dp[ii - 1][jj], dp[ii - 1][jj - 1]) + 1
        else:
            dp[ii][jj] = max(dp[ii - 1][jj], dp[ii - 1][jj - 1])

print(max(dp[T]))