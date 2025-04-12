# https://www.acmicpc.net/problem/16497

from sys import stdin

input = lambda: stdin.readline().rstrip()

loans = [0 for _ in range(32)]
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    for ii in range(start, end):
        loans[ii] += 1

K = int(input())
print(0 if max(loans) > K else 1)
