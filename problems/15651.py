# https://www.acmicpc.net/problem/15651

from sys import stdin
from itertools import product

input = stdin.readline

N, M = map(int, input().split())

for p in product([ii for ii in range(1, N + 1)], repeat=M):
    print(*p)
