# https://www.acmicpc.net/problem/15734

from sys import stdin

input = lambda: stdin.readline().rstrip()

L, R, A = map(int, input().split())

if min(L, R) + A <= max(L, R):
    print((min(L, R) + A) * 2)
else:
    A -= max(L, R) - min(L, R)
    print((max(L, R) + (A // 2)) * 2)
