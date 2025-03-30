# https://www.acmicpc.net/problem/2750

from sys import stdin

input = stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

for a in sorted(arr):
    print(a)
