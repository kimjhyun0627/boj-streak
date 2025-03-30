# https://www.acmicpc.net/problem/14889

from sys import stdin
from itertools import combinations

input = stdin.readline

N = int(input())
members = [list(map(int, input().split())) for _ in range(N)]

res = 10**8
for c in combinations([ii for ii in range(N)], N // 2):
    others = [ii for ii in range(N) if ii not in c]
    diff = abs(
        sum([members[m][n] for m in c for n in c])
        - sum([members[m][n] for m in others for n in others])
    )
    res = min(res, diff)

print(res)
