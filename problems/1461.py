# https://www.acmicpc.net/problem/1461

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

books = list(map(int, input().split()))

positive_pos = sorted([book for book in books if book > 0], reverse=True)
negative_pos = sorted([book for book in books if book < 0])
ans = 0
for ii in range(0, len(positive_pos), M):
    ans += positive_pos[ii] * 2

for ii in range(0, len(negative_pos), M):
    ans -= negative_pos[ii] * 2

print(
    ans
    - max(
        max(positive_pos) if positive_pos else 0,
        -min(negative_pos) if negative_pos else 0,
    )
)
