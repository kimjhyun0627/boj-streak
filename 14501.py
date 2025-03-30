# https://www.acmicpc.net/problem/14501

N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for ii in range(N):
    t, c = works[ii]
    for jj in range(ii + t, N + 1):
        dp[jj] = max(dp[jj], dp[ii] + c)

print(dp[-1])
