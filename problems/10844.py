# https://www.acmicpc.net/problem/10844

from sys import stdin

input = stdin.readline

N = int(input())

dp = [[0 for _ in range(10)]]
for ii in range(1, 10):
    dp[0][ii] = 1

for ii in range(N - 1):
    nums = []
    for jj in range(10):
        if jj == 0:
            nums.append(dp[ii][jj + 1] % 1000000000)
        elif jj == 9:
            nums.append(dp[ii][jj - 1] % 1000000000)
        else:
            nums.append((dp[ii][jj - 1] + dp[ii][jj + 1]) % 1000000000)

    dp.append(nums)

print(sum(dp[-1]) % 1000000000)
