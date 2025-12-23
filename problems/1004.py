# https://www.acmicpc.net/problem/1004

from math import sqrt
from sys import stdin

input = stdin.readline


def is_inside(target_x: int, target_y: int, pos_x: int, pos_y: int, radius: int):
    return sqrt(abs(target_x - pos_x) ** 2 + abs(target_y - pos_y) ** 2) < radius


T = int(input())

for _ in range(T):
    ans = 0
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    for _ in range(N):
        x, y, r = map(int, input().split())
        if is_inside(x1, y1, x, y, r) and not is_inside(x2, y2, x, y, r):
            ans += 1
        if is_inside(x2, y2, x, y, r) and not is_inside(x1, y1, x, y, r):
            ans += 1

    print(ans)
