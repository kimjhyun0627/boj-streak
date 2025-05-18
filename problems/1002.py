# https://www.acmicpc.net/problem/1002

from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        print(-1 if r1 == r2 else 0)
        continue

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d == r1 + r2 or d == abs(r2 - r1):
        print(1)
    elif abs(r2 - r1) < d < r1 + r2:
        print(2)
    else:
        print(0)
