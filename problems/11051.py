# https://www.acmicpc.net/problem/11051

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

dp = [1 for _ in range(N + 1)]

for ii in range(2, N + 1):
    dp[ii] = dp[ii - 1] * (ii)

if K == 0 or K == N:
    print(1)
elif K == 1 or K == N - 1:
    print(N % 10007)
else:
    print((dp[N] // (dp[K] * dp[N - K])) % 10007)
