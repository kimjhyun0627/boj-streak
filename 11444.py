# https://www.acmicpc.net/problem/11444

from sys import stdin, setrecursionlimit

setrecursionlimit(10**9)

memo = {0: 0, 1: 1, 2: 1}


def dp(x):
    if x not in memo:
        if x % 2 == 0:
            memo[x] = (dp(x // 2) * (dp(x // 2) + 2 * dp(x // 2 - 1))) % 1_000_000_007
        else:
            memo[x] = (dp(x // 2) ** 2 + dp(x // 2 + 1) ** 2) % 1_000_000_007
    return memo[x]


n = int(stdin.readline())
print(dp(n))
