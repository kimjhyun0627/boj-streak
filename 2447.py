# https://www.acmicpc.net/problem/2447

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = lambda: stdin.readline().rstrip()


def printer(x, y, n):
    if n == 1:
        canvas[x][y] = True
        return

    k = int(n / 3)
    for ii in range(0, 3):
        for jj in range(0, 3):
            if ii == 1 and jj == 1:
                continue
            printer(x + ii * k, y + jj * k, k)


N = int(input())
canvas = [[False for _ in range(N)] for _ in range(N)]


printer(0, 0, N)

for line in canvas:
    for dot in line:
        print("*" if dot else " ", end="")
    print("")
