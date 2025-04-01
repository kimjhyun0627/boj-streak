# https://www.acmicpc.net/problem/2096

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

min_cand = [0, 0, 0]
max_cand = [0, 0, 0]

for _ in range(N):
    level = list(map(int, input().split()))
    min_cand = [
        level[0] + min(min_cand[:2]),
        level[1] + min(min_cand),
        level[2] + min(min_cand[1:]),
    ]
    max_cand = [
        level[0] + max(max_cand[:2]),
        level[1] + max(max_cand),
        level[2] + max(max_cand[1:]),
    ]

print(max(max_cand), min(min_cand))
