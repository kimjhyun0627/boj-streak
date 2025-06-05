# https://www.acmicpc.net/problem/2725

from sys import stdin

input = lambda: stdin.readline().rstrip()

MAX = 10**6
res = [ii for ii in range(MAX + 1)]

for ii in range(2, MAX + 1):
    if res[ii] == ii:
        for jj in range(ii, MAX + 1, ii):
            res[jj] -= res[jj] // ii

for ii in range(2, MAX + 1):
    res[ii] += res[ii - 1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(res[N] * 2 + 1)
