# https://www.acmicpc.net/problem/15649

from sys import stdin
from itertools import permutations

N, M = map(int, input().split())

for p in permutations([ii for ii in range(1, N + 1)], M):
    print(*p)
