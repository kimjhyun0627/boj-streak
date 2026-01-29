# https://www.acmicpc.net/problem/20529

from itertools import combinations
from sys import stdin

input = stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    mbtis = list(input().split())
    ans = int(1e9)
    if len(mbtis) > 32:
        print(0)
        continue
    else:
        for A, B, C in combinations(mbtis, 3):
            diff = len(set(A + B)) + len(set(B + C)) + len(set(C + A))
            ans = min(ans, diff - (3 * 4))
    print(ans)
