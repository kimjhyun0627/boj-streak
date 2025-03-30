# https://www.acmicpc.net/problem/13549

INF = 10**8

n, k = map(int, input().split())

dp = [INF] * 200001

for ii in range(n + 1):
    dp[ii] = n - ii
    if ii * 2 > n and ii * 2 < len(dp):
        dp[ii * 2] = n - ii

if n < k:
    for ii in range(n + 1, k + 1):
        if ii % 2 == 0:
            dp[ii] = min(dp[ii - 1] + 1, dp[ii + 1] + 1, dp[ii // 2])
        if ii % 2 == 1:
            dp[ii] = min(dp[ii - 1] + 1, dp[ii + 1] + 1)
        if ii * 2 < len(dp):
            dp[ii * 2] = min(dp[ii * 2], dp[ii])

print(dp[k])
