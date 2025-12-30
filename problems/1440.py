# https://www.acmicpc.net/problem/1440

from itertools import permutations
from sys import stdin

input = stdin.readline

digits = list(map(int, input().split(":")))

ans = 0
for h, m, s in permutations(digits, 3):
    if 0 < h <= 12 and 0 <= m < 60 and 0 <= s < 60:
        ans += 1

print(ans)
