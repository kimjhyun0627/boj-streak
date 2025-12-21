# https://www.acmicpc.net/problem/7482

from sys import stdin

input = stdin.readline

N = int(input())

for _ in range(N):
    a = float(input())
    print(f"{a/6:.10f}")
