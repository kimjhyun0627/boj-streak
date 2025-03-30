# https://www.acmicpc.net/problem/15657

from sys import stdin
from itertools import combinations_with_replacement

input = stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for c in combinations_with_replacement(sorted(nums), M):
    print(*c)
