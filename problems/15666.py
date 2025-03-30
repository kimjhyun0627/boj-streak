# https://www.acmicpc.net/problem/15666

from sys import stdin
from itertools import combinations_with_replacement

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
nums = sorted(list(set(list(map(int, input().split())))))

for c in combinations_with_replacement(nums, M):
    print(*c)
