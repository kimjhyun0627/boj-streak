# https://www.acmicpc.net/problem/31909

from sys import stdin

input = stdin.readline

n = int(input())
orders = list(map(int, input().split()))
k = int(input())

keys = [ii for ii in range(8)]
squares = [[2**ii + 2**jj for ii in range(8)] for jj in range(8)]

for o in orders:
    idx = 0
    while idx < len(squares):
        for jj in range(len(squares)):
            if squares[idx][jj] == o:
                keys[idx], keys[jj] = keys[jj], keys[idx]
                idx = 8
                break
        idx += 1

print(keys[k])
