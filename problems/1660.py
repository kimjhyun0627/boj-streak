# https://www.acmicpc.net/problem/1660

from sys import stdin

input = stdin.readline

N = int(input())

m_max = int((6 * N) ** (1/3)) + 3
counts = [m * (m+1) * (m+2) // 6 for m in range(1, m_max) if m * (m+1) * (m+2) // 6 <= N]

dp = [N+1 for ii in range(N+1)]
dp[0] = 0
for ii in range(1, N+1):
    for count in counts:
        if count > ii:
            break
        dp[ii] = min(dp[ii], dp[ii-count]+1)

print(dp[N])