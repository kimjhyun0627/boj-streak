# https://www.acmicpc.net/problem/14651

from sys import stdin

input = lambda: stdin.readline().rstrip()
MOD = 10**9 + 9

N = int(input())

dp = [[0] * 3 for _ in range(N + 1)]

dp[1][1] = 1
dp[1][2] = 1
dp[1][0] = 0

for ii in range(2, N + 1):
    for r in range(3):
        for x in range(3):
            dp[ii][(r + x) % 3] = (dp[ii][(r + x) % 3] + dp[ii - 1][r]) % MOD

print(dp[N][0])
