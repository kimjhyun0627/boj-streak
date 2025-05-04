# https://www.acmicpc.net/problem/4470

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
for ii in range(N):
    print(ii + 1, ". ", input(), sep="")
