# https://www.acmicpc.net/problem/2748

from sys import stdin

input = stdin.readline

N = int(input())
dp = [0 for _ in range(N + 1)]
dp[0], dp[1] = 0, 1

for ii in range(2, N + 1):
    dp[ii] = dp[ii - 1] + dp[ii - 2]

print(dp[-1])
