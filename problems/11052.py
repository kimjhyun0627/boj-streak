# https://www.acmicpc.net/problem/11052

from sys import stdin

input = stdin.readline

N = int(input())
prices = list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]

for ii in range(1, N + 1):
    for jj in range(ii, N + 1):
        dp[jj] = max(dp[jj], dp[jj - ii] + prices[ii - 1])

print(dp[-1])
