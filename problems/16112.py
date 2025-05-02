# https://www.acmicpc.net/problem/16112

from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

res = 0
cur = 0
for obj in sorted(
    dict(enumerate(list(map(int, input().split())))).items(), key=lambda x: x[1]
):
    res += obj[1] * cur
    if cur < K:
        cur += 1

print(res)
