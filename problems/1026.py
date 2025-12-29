# https://www.acmicpc.net/problem/1026

from sys import stdin

input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)

ans = 0
for ii in range(N):
    ans += A[ii] * B[ii]

print(ans)
