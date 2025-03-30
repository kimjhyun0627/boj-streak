# https://www.acmicpc.net/problem/32184

from sys import stdin

input = lambda: stdin.readline().rstrip()

A, B = map(int, input().split())

cnt = 0
for ii in range(A, B + 1):
    if ii % 2:
        cnt += 1
    else:
        if ii == A:
            cnt += 1

print(cnt)
