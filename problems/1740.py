# https://www.acmicpc.net/problem/1740

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = bin(int(input()))[2:]

res, tmp = 0, 1
for ii in reversed(N):
    res += int(ii) * tmp
    tmp *= 3

print(res)
