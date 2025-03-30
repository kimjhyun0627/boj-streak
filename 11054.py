# https://www.acmicpc.net/problem/11054

from sys import stdin

input = stdin.readline

N = int(input())
up_arr = list(map(int, input().split()))
dn_arr = up_arr[::-1]

up_dp = [1 for _ in range(N)]
dn_dp = [1 for _ in range(N)]
res_dp = [0 for _ in range(N)]

for ii in range(N):
    for jj in range(ii):

        if up_arr[ii] > up_arr[jj]:
            up_dp[ii] = max(up_dp[ii], up_dp[jj] + 1)

        if dn_arr[ii] > dn_arr[jj]:
            dn_dp[ii] = max(dn_dp[ii], dn_dp[jj] + 1)

for ii in range(N):
    res_dp[ii] = up_dp[ii] + dn_dp[N - ii - 1] - 1

print(max(res_dp))
