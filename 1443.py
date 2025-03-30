# https://www.acmicpc.net/problem/1443

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


def dfs(value, count, idx):
    res = -1
    if len(str(value)) > D:
        return res
    if count == P and len(str(value)) <= D:
        res = value

    for ii in range(idx, 1, -1):
        res = max(res, dfs(value * ii, count + 1, ii))

    return res


D, P = map(int, input().split())

print(dfs(1, 0, 9))
