# https://www.acmicpc.net/problem/30805

from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

res = []

while True:
    sorted_A = sorted(A, reverse=True)
    max_A = -1
    for a in sorted_A:
        if a in B:
            max_A = a
            break

    if max_A == -1:
        break

    res.append(max_A)
    idx_A = A.index(max_A)
    idx_B = B.index(max_A)
    B = B[idx_B + 1 :]
    A = A[idx_A + 1 :]

print(len(res))
print(*res)
