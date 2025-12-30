# https://www.acmicpc.net/problem/15739

from sys import stdin

input = stdin.readline

N = int(input())
square = [list(map(int, input().split())) for _ in range(N)]

ans = "TRUE"

for ii in range(1, N**2 + 1):
    if ii not in [s for sq in square for s in sq]:
        ans = "FALSE"
        break

sq_sum = N * (N**2 + 1) / 2
for ii in range(N):
    if sum([square[ii][jj] for jj in range(N)]) != sq_sum:
        ans = "FALSE"
        break
    if sum([square[jj][ii] for jj in range(N)]) != sq_sum:
        ans = "FALSE"
        break
if sum([square[ii][ii] for ii in range(N)]) != sq_sum:
    ans = "FALSE"
if sum([square[ii][N - ii - 1] for ii in range(N)]) != sq_sum:
    ans = "FALSE"

print(ans)
