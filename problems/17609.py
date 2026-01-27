# https://www.acmicpc.net/problem/17609

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

T = int(input())
candidates = [input().strip() for _ in range(T)]


def is_same(l, r, chance):
    while l < r:
        if candidate[l] == candidate[r]:
            l += 1
            r -= 1
        elif chance == 0:
            return min(is_same(l + 1, r, 1), is_same(l, r - 1, 1))
        else:
            return 2
    return chance


for candidate in candidates:
    print(is_same(0, len(candidate) - 1, 0))
