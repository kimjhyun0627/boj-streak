# https://www.acmicpc.net/problem/11055

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
seq = list(map(int, input().split()))
dp = [s for s in seq]

for ii in range(N):
    for jj in range(ii):
        if seq[ii] > seq[jj]:
            dp[ii] = max(dp[ii], dp[jj] + seq[ii])

print(max(dp))
