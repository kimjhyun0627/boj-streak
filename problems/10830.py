# https://www.acmicpc.net/problem/10830

from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)
input = lambda: stdin.readline().rstrip()


N, B = map(int, input().split())
matrix = [[ii % 1000 for ii in list(map(int, input().split()))] for _ in range(N)]
matrixes = dict({1: matrix})


def multiply(mat, n):
    if n in matrixes:
        return matrixes[n]

    new_mat = [[0 for _ in range(N)] for _ in range(N)]
    small_mat = multiply(mat, n // 2)
    big_mat = multiply(mat, n // 2 + n % 2)
    for ii in range(N):
        for jj in range(N):
            for kk in range(N):
                new_mat[ii][jj] += small_mat[ii][kk] * big_mat[kk][jj]
            new_mat[ii][jj] %= 1000

    matrixes[n] = new_mat
    return new_mat


for m in multiply(matrix, B):
    print(*m)
