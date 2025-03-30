# https://www.acmicpc.net/problem/13707

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
dp[0][0] = 1

for ii in range(1, K + 1):
    for jj in range(N + 1):
        dp[ii][jj] = (dp[ii - 1][jj] + dp[ii][jj - 1]) % 1000000000

print(dp[K][N])
