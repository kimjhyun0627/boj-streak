# https://www.acmicpc.net/problem/11722

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
seq = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for ii in range(N):
    for jj in range(ii):
        if seq[jj] > seq[ii]:
            dp[ii] = max(dp[ii], dp[jj] + 1)

print(max(dp))
