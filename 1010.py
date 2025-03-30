# https://www.acmicpc.net/problem/1010

from sys import stdin
from itertools import combinations

input = stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    res = 1
    for ii in range(N):
        res *= M - ii
        res //= ii + 1

    print(res)
