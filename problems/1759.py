# https://www.acmicpc.net/problem/1759

from sys import stdin
from itertools import combinations

input = stdin.readline

L, C = map(int, input().split())
chars = input().split()
chars.sort()

for c in combinations(chars, L):
    if (sum([c.count(v) for v in ["a", "e", "i", "o", "u"]])) < 1:
        continue
    if (L - sum([c.count(v) for v in ["a", "e", "i", "o", "u"]])) < 2:
        continue
    print("".join(c))
