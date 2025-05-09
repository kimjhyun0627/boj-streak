# https://www.acmicpc.net/problem/4159

from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    N = int(input())
    if N == 0:
        break

    gas = []
    for _ in range(N):
        gas.append(int(input()))

    res = "POSSIBLE"
    cur = 0
    for g in sorted(gas):
        if g - cur > 200:
            res = "IMPOSSIBLE"
            break
        cur = g

    if (1422 - cur) * 2 > 200:
        res = "IMPOSSIBLE"

    print(res)
