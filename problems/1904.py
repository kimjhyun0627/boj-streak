# https://www.acmicpc.net/problem/1904

from sys import stdin

input = stdin.readline

N = int(input())
dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2

for ii in range(3, N + 1):
    dp[ii] = (dp[ii - 1] + dp[ii - 2]) % 15746

print(dp[N])
