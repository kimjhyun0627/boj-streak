# https://www.acmicpc.net/problem/9251

from sys import stdin

input = stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for ii in range(1, len(str1) + 1):
    for jj in range(1, len(str2) + 1):
        if str1[ii - 1] == str2[jj - 1]:
            dp[ii][jj] = dp[ii - 1][jj - 1] + 1
        else:
            dp[ii][jj] = max(dp[ii - 1][jj], dp[ii][jj - 1])

print(dp[-1][-1])