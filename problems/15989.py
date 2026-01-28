# https://www.acmicpc.net/problem/15989

from sys import stdin

input = stdin.readline

T = int(input())
cases = [int(input()) for _ in range(T)]

dp = [0 for _ in range(10001)]
for ii in range(1, len(dp)):
    if ii < 4:
        dp[ii] = ii
        continue
    dp[ii] = dp[ii - 3] + ii // 2 + 1

for n in cases:
    print(dp[n])
