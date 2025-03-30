# https://www.acmicpc.net/problem/15652

from sys import stdin
from itertools import combinations_with_replacement

input = stdin.readline

N, M = map(int, input().split())
for p in combinations_with_replacement([ii for ii in range(1, N + 1)], M):
    print(*p)
