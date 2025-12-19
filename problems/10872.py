# https://www.acmicpc.net/problem/10872

from sys import stdin

input = stdin.readline

N = int(input())

ans = 1

for ii in range(1, N + 1):
    ans *= ii

print(ans)
