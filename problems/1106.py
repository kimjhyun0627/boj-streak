# https://www.acmicpc.net/problem/1106

from sys import stdin

input = stdin.readline

C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]

dp = [
    10**8 if ii != 0 else 0
    for ii in range(C + max(customers for _, customers in costs) + 1)
]
for ii in range(1, C + max(customers for _, customers in costs) + 1):
    for cost, customer in costs:
        if ii >= customer:
            dp[ii] = min(dp[ii], dp[ii - customer] + cost)


# print(dp)
print(min(dp[C:]))
