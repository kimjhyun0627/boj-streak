# https://www.acmicpc.net/problem/1182

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline


def dfs(idx, sum):
    cnt = 0
    if sum == S and idx >= 1:
        cnt += 1

    for ii in range(idx, N):
        sum += arr[ii]
        cnt += dfs(ii + 1, sum)
        sum -= arr[ii]

    return cnt


N, S = map(int, input().split())
arr = sorted(list(map(int, input().split())))

print(dfs(0, 0))
