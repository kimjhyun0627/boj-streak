# https://www.acmicpc.net/problem/32141

from sys import stdin

input = stdin.readline

n, h = map(int, input().rstrip().split())
cards = list(map(int, input().rstrip().split()))

res = 0

for c in sorted(cards):
    if h <= 0:
        break
    h -= c
    res += 1

print(-1 if res == n and h > 0 else res)