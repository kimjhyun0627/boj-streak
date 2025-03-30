# https://www.acmicpc.net/problem/11660

from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())
table = [list(map(int, input().rstrip().split())) for _ in range(n)]
sums = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for ii in range(1, n+1):
    for jj in range(1, n+1):
        sums[ii][jj] = sums[ii-1][jj] + sums[ii][jj-1] - sums[ii-1][jj-1] + table[ii-1][jj-1]

for _ in range(m):
    fx, fy, tx, ty = map(int, input().rstrip().split())
    print(sums[tx][ty] - sums[tx][fy-1] - sums[fx-1][ty] + sums[fx-1][fy-1])
