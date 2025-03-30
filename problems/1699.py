# https://www.acmicpc.net/problem/1699

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

dp = [ii for ii in range(N + 1)]

for ii in range(2, N + 1):
    for n in range(1, ii + 1):
        sq = n**2
        if sq > ii:
            break
        dp[ii] = min(dp[ii], dp[ii - sq] + 1)

print(dp[-1])
