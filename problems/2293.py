# https://www.acmicpc.net/problem/2293

from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins = [ii for ii in coins if ii <= K]

dp = [0 for _ in range(10001)]

for c in coins:
    dp[c] += 1
    for ii in range(c, K + 1):
        dp[ii] += dp[ii - c]

print(dp[K])
