# https://www.acmicpc.net/problem/2565

from sys import stdin

input = stdin.readline

N = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
dp = [1 for _ in range(N)]

for ii in range(N):
    for jj in range(ii):
        if lines[ii][1] > lines[jj][1]:
            dp[ii] = max(dp[ii], dp[jj] + 1)

print(N - max(dp))
