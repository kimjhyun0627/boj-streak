# https://www.acmicpc.net/problem/1025

from itertools import product
from math import sqrt
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
table = [list(input().rstrip()) for _ in range(N)]

if N == M == 1:
    print(int(table[0][0]) if sqrt(int(table[0][0])).is_integer() else -1)
    exit(0)

ans = -1
for sx, gx in product(range(N), repeat=2):
    for sy, gy in product(range(M), repeat=2):
        if gx == gy == 0:
            continue

        for ii in range(4):
            x = -gx if ii//2 == 0 else gx
            y = -gy if ii%2 == 0 else gy
            arr = []
            h = 0
            while 0<=sx+x*h<N and 0<=sy+y*h<M:
                arr.append(table[sx+x*h][sy+y*h])
                h += 1

            for ii in range(1, len(arr)+1):
                cand = int(''.join(map(str, arr[:ii])))
                if sqrt(cand).is_integer():
                    ans = max(ans, cand)
print(ans)