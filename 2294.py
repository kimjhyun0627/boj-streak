# https://www.acmicpc.net/problem/2294

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

dp = [10**8 for _ in range(K + 1)]
dp[0] = 0
for c in coins:
    if c <= K:
        dp[c] = c

for c in coins:
    for ii in range(c, K + 1):
        dp[ii] = min(dp[ii], dp[ii - c] + 1)

print(dp[K] if dp[K] != 10**8 else -1)
